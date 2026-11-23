"""Wiki 健康檢查（AGENTS.md 第 4 節 Lint）。

用法：python tools/lint_wiki.py
只用 Python 標準函式庫。全部通過印出「Lint 通過」；否則列出問題並以非 0 結束。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TYPES = {"source", "concept", "overview", "query"}
SKIP = {"index.md", "log.md"}  # 目錄與紀錄頁不需要 front matter

problems = []
pages = {}

def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data

for f in sorted(WIKI.rglob("*.md")):
    rel = f.relative_to(WIKI).as_posix()
    text = f.read_text(encoding="utf-8")
    pages[rel] = text
    if f.name in SKIP:
        continue
    fm = front_matter(text)
    if fm is None:
        problems.append(f"{rel}：缺少 front matter")
        continue
    for key in ("title", "type", "sources", "updated"):
        if key not in fm:
            problems.append(f"{rel}：front matter 缺少 {key}")
    if fm.get("type") not in TYPES:
        problems.append(f"{rel}：type 必須是 {sorted(TYPES)}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm.get("updated", "")):
        problems.append(f"{rel}：updated 格式應為 YYYY-MM-DD")
    ids = [s.strip() for s in fm.get("sources", "").strip("[]").split(",") if s.strip()]
    if fm.get("type") == "concept" and not ids:
        problems.append(f"{rel}：概念頁至少要依據一份資料")
    for sid in ids:
        if not (WIKI / "sources" / f"{sid}.md").exists():
            problems.append(f"{rel}：sources 裡的 {sid} 沒有對應的 wiki/sources/{sid}.md")

# 相對連結
linked = set()
for rel, text in pages.items():
    here = (WIKI / rel).parent
    for href in re.findall(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)", text):
        if href.startswith("http"):
            continue
        target = (here / href).resolve()
        if not target.exists():
            problems.append(f"{rel}：連結失效 {href}")
        elif WIKI in target.parents or target.parent == WIKI:
            linked_rel = target.relative_to(WIKI).as_posix()
            if linked_rel != rel:
                linked.add(linked_rel)

# index 收錄與孤兒頁
index = pages.get("index.md", "")
for rel in pages:
    if rel in SKIP:
        continue
    if f"]({rel})" not in index:
        problems.append(f"index.md 沒有收錄 {rel}")
    if rel not in linked:
        problems.append(f"{rel}：孤兒頁（沒有任何頁面連到它）")

if problems:
    print(f"Lint 發現 {len(problems)} 個問題：")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"Lint 通過：{len(pages)} 個 Wiki 頁面。")
