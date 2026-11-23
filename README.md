# Token LLM Wiki｜AI 怎麼讀文字

用「先討論、後生成」的方式建立的 LLM Wiki，主題是 **Token：LLM 怎麼讀文字**，並用這個 Wiki 產生一份給新手的教學 HTML 簡報。

- 教學簡報：https://andreajang0223-ops.github.io/token-llm-wiki/slides/
- Wiki 目錄：[wiki/index.md](wiki/index.md)（從 [wiki/overview.md](wiki/overview.md) 開始讀）
- 工作規則：[AGENTS.md](AGENTS.md)（Claude Code 讀 [CLAUDE.md](CLAUDE.md)）
- 流程設計：[docs/workflow.md](docs/workflow.md)
- 執行紀錄：[runs/2026-11-23-run1.md](runs/2026-11-23-run1.md)

## 結構
```
raw/        原始資料登記（sources.md）與自己的 tokenizer 實驗（experiment/）
wiki/       sources/（8 份資料）、concepts/（11 個概念）、overview、queries、index、log
slides/     教學簡報（單一 HTML，只從 wiki/ 取材）
tools/      lint_wiki.py、check_slides.py、check_layout.mjs
docs/       loop／graph 流程圖
runs/       每次執行的紀錄
```

## 檢查指令
```
python tools/lint_wiki.py        # Wiki 健康檢查
python tools/check_slides.py     # 簡報每頁都有依據、數字都對得上
node tools/check_layout.mjs      # 簡報版面不超出（需要 Playwright）
```

雲科大 工設碩一 張芫瑞｜生成式 AI 課程第十週作業
