"""簡報內容檢查（AGENTS.md 第 4 節 Make slides 第 5 步）。

用法：python tools/check_slides.py [slides/index.html]
檢查：
  1. 頁數與 wiki/queries/ 最新大綱的頁數一致
  2. 每頁 <section class="slide"> 都有 data-sources，且指向存在的 wiki/ 頁面
  3. 簡報上出現的每個數字，都能在該頁引用的 Wiki 頁裡找到（逗號忽略）
只用 Python 標準函式庫。全部通過印出「簡報檢查通過」，否則列出問題並以非 0 結束。
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "slides/index.html")


class SlideParser(HTMLParser):
    """收集每個 section.slide 的 data-sources 與可見文字（略過 <script>、<style>）。"""

    def __init__(self):
        super().__init__()
        self.slides, self.depth, self.skip = [], 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "section" and "slide" in (a.get("class") or "").split():
            self.slides.append({"id": a.get("id", f"#{len(self.slides) + 1}"),
                                "sources": a.get("data-sources", ""), "text": []})
            self.depth = 1
        elif self.depth and tag == "section":
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if self.depth and tag == "section":
            self.depth -= 1

    def handle_data(self, data):
        if self.depth and not self.skip:
            self.slides[-1]["text"].append(data)


NUM = re.compile(r"(?<![\w.\-])\d[\d,]*(?:\.\d+)?(?![\w])")


def numbers(text):
    return {n.replace(",", "").rstrip(".") for n in NUM.findall(text)}


problems = []
parser = SlideParser()
parser.feed(SLIDES.read_text(encoding="utf-8"))
slides = parser.slides

outlines = sorted((ROOT / "wiki/queries").glob("*slides-outline.md"))
if outlines:
    rows = re.findall(r"^\| (\d+) \|", outlines[-1].read_text(encoding="utf-8"), re.M)
    if len(rows) != len(slides):
        problems.append(f"頁數不符：大綱 {outlines[-1].name} 有 {len(rows)} 頁，簡報有 {len(slides)} 頁")

for i, s in enumerate(slides, 1):
    label = f"第 {i} 頁（{s['id']}）"
    paths = [p.strip() for p in s["sources"].split(",") if p.strip()]
    if not paths:
        problems.append(f"{label}：缺少 data-sources")
        continue
    corpus = ""
    for p in paths:
        f = ROOT / p
        if not p.startswith("wiki/"):
            problems.append(f"{label}：data-sources 只能引用 wiki/ 內的頁面（{p}）")
        elif not f.exists():
            problems.append(f"{label}：引用的頁面不存在（{p}）")
        else:
            corpus += f.read_text(encoding="utf-8")
    text = " ".join(s["text"])
    missing = sorted(numbers(text) - numbers(corpus), key=lambda x: (len(x), x))
    if missing:
        problems.append(f"{label}：這些數字在引用的 Wiki 頁裡找不到 → {', '.join(missing)}")

if problems:
    print(f"簡報檢查發現 {len(problems)} 個問題：")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"簡報檢查通過：{len(slides)} 頁，每頁都有依據，數字都能在引用的 Wiki 頁找到。")
