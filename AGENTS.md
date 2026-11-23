# AGENTS.md｜Token LLM Wiki 的工作規則

這個 repo 是一個由 AI 維護的 **LLM Wiki**，主題是「Token：LLM 怎麼讀文字」。
人負責挑資料、提問題、做決定；AI 負責整理、交叉連結、檢查與產生成品。
**動手之前請完整讀完本文件。**（Claude Code 讀 `CLAUDE.md`，內容指向本文件。）

---

## 1. 三層結構

| 層 | 資料夾 | 誰寫 | 規則 |
|---|---|---|---|
| 原始資料 | `raw/` | 人提供、AI 只記錄 | 不修改。`raw/sources.md` 登記每份資料的網址與取得日期；原文有版權，不整份複製進 repo |
| Wiki | `wiki/` | AI | 所有知識都整理成這裡的 Markdown 頁面，彼此用相對連結串起來 |
| 成品 | `slides/` | AI | 只能從 `wiki/` 取材，不可以直接引用 `raw/` 或自己的記憶 |

另外：`tools/`（檢查程式）、`docs/workflow.md`（流程圖）、`runs/`（每次執行的紀錄）。

## 2. Wiki 頁面格式

每一頁開頭都有 YAML front matter：

```yaml
---
title: BPE（位元組對編碼）
type: concept        # source｜concept｜overview｜query
sources: [s02-hf-bpe-course, s05-wikipedia-bpe]   # 這頁依據的 source 頁 id
updated: 2026-11-23
---
```

- `wiki/sources/`：一份資料一頁，檔名 `sNN-簡短英文.md`。內容：基本資訊、重點摘要（用自己的話）、可引用的數字、這份資料的限制。
- `wiki/concepts/`：一個概念一頁，檔名小寫英文加連字號。內容必須能回答「這是什麼、為什麼重要、例子」，最後有「相關頁面」與「依據」。
- `wiki/overview.md`：整個主題的總覽與建議閱讀順序。
- `wiki/queries/`：重要的提問與回答存成一頁，日期開頭，例如 `2026-11-23-slides-outline.md`。
- `wiki/index.md`：全部頁面的目錄，一頁一行加一句說明。
- `wiki/log.md`：只往下新增的工作紀錄，格式 `## [YYYY-MM-DD] 動作｜對象`。

## 3. 寫作規則

1. **先討論、後生成**：新增資料或做成品之前，先和使用者確認目的、讀者與範圍，把決定寫進 `log.md`，再開始寫。
2. **每個事實都要有依據**：概念頁裡的數字與說法，必須出自 `sources` 欄位列出的 source 頁；source 頁的數字必須出自原始資料。
3. **推論要標示**：不是資料直接寫的、而是 AI 推出來的說法，前面加「（推論）」。
4. **資料互相矛盾時**：兩種說法都寫，註明來源，不要自己選一個。
5. **不知道就寫不知道**：找不到依據的數字寫「本 Wiki 尚無資料」，不可編造。
6. 語言用繁體中文，術語第一次出現附英文。讀者假設是完全沒接觸過 AI 的人。

## 4. 操作流程

### Ingest（收錄一份新資料）
1. 在 `raw/sources.md` 登記網址、類型與取得日期。
2. 讀資料，寫一頁 `wiki/sources/sNN-*.md`。
3. 更新或新增相關的概念頁（一份資料通常會動到 3–6 頁），把新資訊和既有內容對照，有矛盾就照規則 4 處理。
4. 更新 `wiki/index.md`，在 `wiki/log.md` 記一筆。
5. 執行 `python tools/lint_wiki.py`，有錯就修到通過。

### Query（向 Wiki 提問）
1. 先讀 `wiki/index.md` 找相關頁，再讀那些頁回答，回答要附頁面連結。
2. 值得留下的回答存進 `wiki/queries/`，並更新 index 與 log。
3. 回答時發現 Wiki 缺資料，就記在 log 的「待補」並告訴使用者，不要用記憶補。

### Lint（健康檢查）
`python tools/lint_wiki.py` 會檢查：front matter 欄位、`sources` 指到的頁面存在、相對連結沒有斷、每頁都有被 index 收錄、沒有孤兒頁（沒有任何頁連到它）、概念頁至少依據一份資料。

### Make slides（從 Wiki 做教學簡報）
1. **討論**：確認聽眾、長度、重點，記入 log。
2. **Query**：從 index 找頁面，產生大綱存成 `wiki/queries/日期-slides-outline.md`，每一頁簡報對應到 Wiki 頁面。
3. **檢查大綱**：每頁都有對應的 Wiki 頁；如果某頁找不到依據，回到 Ingest 補資料，不要硬寫。
4. **生成**：寫 `slides/index.html`。每個 `<section class="slide">` 必須有 `data-sources`，列出依據的 Wiki 頁路徑（從 repo 根目錄算起）。
5. **檢查成品**：
   - `python tools/check_slides.py`：引用的頁面存在；簡報上的每個數字都能在它引用的 Wiki 頁找到。
   - `node tools/check_layout.mjs`：1280×720 與手機寬度下，每頁內容都沒有超出版面。
6. 檢查不通過時，**只重新生成出錯的那幾頁**，再跑一次檢查；全部通過才算完成。
7. 把這次執行的過程、檢查結果與修正寫成 `runs/日期-*.md`。

## 5. 簡報規則

- 一頁只講一件事；標題用一句完整的話說出重點。
- 先給例子再給術語；每頁文字不超過 60 字（不含例子方塊）。
- 單一 HTML 檔，不用外部框架；鍵盤左右鍵、點擊、滑動都能換頁；手機上也能看。
- 最後一頁放資料來源，連回 Wiki。
