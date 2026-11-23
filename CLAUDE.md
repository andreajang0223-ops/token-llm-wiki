# CLAUDE.md

本專案的工作規則寫在 [AGENTS.md](AGENTS.md)，請先完整閱讀並照做。

最重要的四條：

1. 先討論、後生成：做任何新增或成品之前，先和使用者確認目的與讀者，並記入 `wiki/log.md`。
2. 簡報只能從 `wiki/` 取材，每頁要用 `data-sources` 標示依據。
3. 每個數字都要有依據；推論要標「（推論）」；不知道就寫「本 Wiki 尚無資料」。
4. 改完一定要跑 `python tools/lint_wiki.py`；做簡報還要跑 `python tools/check_slides.py` 與 `node tools/check_layout.mjs`。
