# 實驗：用兩種 tokenizer 切 13 段文字

- 套件：`npm install gpt-tokenizer@2.9.0`（內含 o200k_base、cl100k_base 編碼表，可離線執行）
- 執行：`node tokenize_examples.cjs > output.jsonl 2> vocab_size.txt`
- `output.jsonl`：每行一段文字，含字元數、位元組數、兩種編碼的 token 數、編號與每個 token 的內容。
  無法單獨顯示成字的 token 以 `<十六進位位元組>` 表示，例如 `<e9 a0>`。
- `vocab_size.txt`：套件回報的詞彙表大小。

## 修正紀錄
第一版程式用 `decode([單一編號])` 逐一還原每個 token，結果把「半個中文字」錯誤地算到下一個 token 上
（例如把「頸」的最後一個位元組顯示成完整的「頸」）。原因是套件的 decode 會在多次呼叫之間暫存未完成的位元組。
第二版改為直接讀取每個 token 的原始位元組，結果見 output.jsonl。
