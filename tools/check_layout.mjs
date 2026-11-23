// 簡報版面檢查（AGENTS.md 第 4 節 Make slides 第 5 步）
// 用法：node tools/check_layout.mjs   （需要 Playwright：npm i playwright）
// 在 1280×720 與手機（390×844）兩種視窗下逐頁檢查：內容是否超出投影片、頁面是否出現水平捲動。
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const url = pathToFileURL(path.join(root, 'slides/index.html')).href;
const viewports = [{ name: '1280×720', width: 1280, height: 720 }, { name: '手機 390×844', width: 390, height: 844 }];
const problems = [];

const browser = await chromium.launch();
for (const vp of viewports) {
  const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
  await page.goto(url);
  await page.waitForTimeout(300);
  const count = await page.evaluate(() => document.querySelectorAll('section.slide').length);
  for (let i = 0; i < count; i++) {
    const r = await page.evaluate(async (i) => {
      window.deck.go(i);
      await new Promise((ok) => setTimeout(ok, 50));
      const s = document.querySelectorAll('section.slide')[i];
      const over = [];
      for (const el of s.querySelectorAll('*')) {
        const b = el.getBoundingClientRect(), box = s.getBoundingClientRect();
        if (b.width && (b.right > box.right + 1 || b.bottom > box.bottom + 1)) over.push(el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : ''));
      }
      return { id: s.id, sh: s.scrollHeight, ch: s.clientHeight, sw: s.scrollWidth, cw: s.clientWidth,
               pageW: document.documentElement.scrollWidth, winW: window.innerWidth, over: [...new Set(over)].slice(0, 4) };
    }, i);
    if (r.sh > r.ch + 1 || r.sw > r.cw + 1 || r.over.length)
      problems.push(`${vp.name} 第 ${i + 1} 頁（${r.id}）內容超出投影片：${r.over.join('、') || `${r.sh}>${r.ch}`}`);
    if (r.pageW > r.winW + 1) problems.push(`${vp.name} 第 ${i + 1} 頁出現水平捲動`);
  }
  await page.close();
}
await browser.close();

if (problems.length) {
  console.log(`版面檢查發現 ${problems.length} 個問題：`);
  problems.forEach((p) => console.log(' -', p));
  process.exit(1);
}
console.log(`版面檢查通過：${viewports.map((v) => v.name).join('、')} 下每頁都沒有超出。`);
