# 工作紀錄（只往下新增）

## [2026-11-23] 討論｜主題與範圍
- AI 依作業要求提出三個主題：Token 是什麼、3D 列印公差與配合、設計專利入門。
- 使用者選擇「Token 是什麼：LLM 怎麼讀文字」。
- AI 先找到 7 份可用資料（官方說明、教學課程、技術文件、開源專案、百科、論文、演講），並提議加一份自己的 tokenizer 實驗，讓中文與英文的比較有實際數字。

## [2026-11-23] 討論｜簡報的讀者與長度
- 使用者決定：讀者是「完全沒接觸過 AI 的人」，簡報約 12 頁、10 分鐘。
- 影響：Wiki 的概念頁要先給例子與比喻再給術語；BPE 只講到「把常一起出現的兩塊黏起來」的程度。

## [2026-11-23] Ingest｜s01 OpenAI：What are tokens
- 新增：sources/s01、concepts/token、concepts/cost-and-languages、concepts/context-window、index。
- Lint 第一次未通過（5 個問題）：概念頁先連到了還沒建立的頁面（overview、letters-and-spelling、s08）。
- 修正：建立 overview；尚未建立的頁面先不連結，改記為待補。
- 待補：中文的 token 數字（預計由 s08 實驗補上）；「AI 數不清字母」需要找到切法的實際例子。

## [2026-11-23] Ingest｜s02 Hugging Face BPE 課程
- 新增：sources/s02、concepts/bpe、concepts/bytes-and-chinese；更新 token、overview、index。
- 新資訊與既有內容沒有矛盾。BPE 的比喻（樂高）標為推論。

## [2026-11-23] Ingest｜s03 Hugging Face：Summary of the tokenizers
- 新增：sources/s03、concepts/tokenization-levels、concepts/vocabulary；更新 bpe（誰在用、其他演算法）、bytes-and-chinese（SentencePiece 與不用空格的語言）、token、overview、index。
- 與 s02 一致：兩者都說 GPT-2 用 byte-level BPE、基本詞彙 256。

## [2026-11-23] Ingest｜s04 openai/tiktoken
- 新增：sources/s04、concepts/tokenizer；更新 token（模型看的是編號、encod + ing 例子）、overview、index。
- 修正：bytes-and-chinese 原本寫「現在的 tokenizer 大多從位元組開始切」，資料只支持「GPT-2 等模型」，改成有依據的說法。

## [2026-11-23] Ingest｜s05 Wikipedia：Byte-pair encoding
- 新增：sources/s05；更新 bpe（加上起源與壓縮例子）、vocabulary（GPT-3.5／GPT-4 的 100,258）、bytes-and-chinese（先轉 UTF-8 位元組）、index。
- 對照：s05 的 GPT-2 使用 byte-level BPE，與 s02、s03 一致。vocabulary 新增一句「詞彙表越大切得越少」，資料沒有直接寫，標為推論，等 s08 實驗驗證。

## [2026-11-23] Ingest｜s06 Sennrich 2016 論文
- 新增：sources/s06；更新 bpe（年表）、tokenization-levels（子詞解決沒看過的字）、index、overview。
- 限制：只讀摘要，已在 source 頁註明。

## [2026-11-23] Ingest｜s07 39C3 演講 51 Ways to Spell the Image Giraffe
- 新增：sources/s07、concepts/token-politics；更新 vocabulary（詞彙表反映資料組成）、overview、index。
- 演講的「不中立」屬於講者觀點，在 source 與概念頁都註明是主張。
- 順手修正：tokenization-levels 原本寫「現在的 AI 幾乎都用子詞」，改成「本 Wiki 收錄的模型」，避免超出資料範圍。
- 待補：giraffe 在實際 tokenizer 中怎麼被切（由 s08 實驗補）。

## [2026-11-23] Ingest｜s08 自己的實驗（gpt-tokenizer）
- 檢查實驗輸出時發現錯誤：第一版程式逐一 decode 每個 token，套件會在呼叫之間暫存未完成的位元組，導致「頸」的最後一個位元組被顯示成完整的「頸」，看起來像前一塊是空的。改成直接讀每個 token 的原始位元組後重跑，並在 raw/experiment/README.md 記錄。
- 新增：sources/s08、concepts/letters-and-spelling；更新 cost-and-languages（中英對照表）、bytes-and-chinese（半個字的實例）、vocabulary（套件回報的詞彙表大小）、token-politics（giraffe 的實際切法）、token、overview（三個最重要的發現）、index。
- 發現矛盾：s05 說 GPT-3.5／GPT-4 詞彙表 100,258，套件回報 cl100k_base 是 100,264。依規則兩者並列，不自行判斷。
- 驗證推論：vocabulary 的「詞彙表越大切得越少」得到實驗支持，但樣本少，仍標推論。
- 待補已完成：中文 token 數字、giraffe 的實際切法、strawberry 的切法。

## [2026-11-23] Query｜教學簡報大綱
- 依「讀者完全沒接觸過 AI、12 頁、10 分鐘」的決定，從 index 與 overview 查詢，產生 queries/2026-11-23-slides-outline.md。
- 檢查大綱：12 頁都有依據；第 2 頁屬推論、第 10 頁不寫最新上限，已在大綱註明。不需要回到 Ingest。

## [2026-11-23] Make slides｜第一次產生簡報（12 頁）
- 內容檢查第 1 次：第 2 頁的「3」找不到依據。原因是概念頁寫國字「三塊」，阿拉伯數字只在 s08 的表格裡。修正：第 2 頁的 data-sources 補上 s08，重跑通過。
- 版面檢查第 1 次：程式找不到 Playwright（ESM 匯入路徑問題），屬於工具錯誤；改用 createRequire 後通過。為了確認檢查真的有效，另外在副本塞入過長文字，檢查正確回報第 9 頁超出。
- 人工看圖：封面的積木例子「AI｜␣怎麼｜讀｜文字｜？」是 AI 自己想像的切法，不是實驗結果；兩個自動檢查都沒抓到（裡面沒有數字）。修正：改用 s08 的「人工智慧 → 人工｜智慧」。另外字太小、頁碼按鈕壓到頁尾，一併調整，重跑兩個檢查都通過。
- 調整流程：AGENTS.md 的 Make slides 加入「人工看圖」步驟；簡報規則加入「切法示範只能用實驗結果」；新增第 6 節實驗規則（讀原始位元組）。
