---
title: 自己的實驗：用兩種 tokenizer 切 13 段文字
type: source
sources: []
updated: 2026-11-23
---

# s08｜自己的實驗：用兩種 tokenizer 切 13 段文字

- 類型：實驗（本 repo 產生的資料，完整保存在 `raw/experiment/`）
- 工具：npm 套件 gpt-tokenizer 2.9.0，內含 `o200k_base` 與 `cl100k_base` 兩種編碼（s04 提到的兩種），在本機離線執行
- 程式：`raw/experiment/tokenize_examples.cjs`；原始輸出：`raw/experiment/output.jsonl`
- 執行：2026-11-23

## 結果
「␣」代表空格；`<e9 a0>` 這種寫法代表**不完整的位元組**：一個中文字在 UTF-8 裡占 3 個位元組，有時會被拆到兩個 token 裡，單獨一塊顯示不出字。

| 文字 | 字元 | 位元組 | o200k_base | cl100k_base | o200k_base 的切法 |
|---|---|---|---|---|---|
| Hello world | 11 | 11 | 2 | 2 | Hello │ ␣world |
| tokenization | 12 | 12 | 2 | 2 | token │ ization |
| strawberry | 10 | 10 | 3 | 3 | st │ raw │ berry |
| giraffe | 7 | 7 | 3 | 3 | g │ ira │ ffe |
| ␣giraffe | 8 | 8 | 2 | 2 | ␣gira │ ffe |
| 人工智慧 | 4 | 12 | 2 | 6 | 人工 │ 智慧 |
| 我喜歡吃蘋果 | 6 | 18 | 7 | 11 | 我 │ 喜 │ 歡 │ 吃 │ `<e8 98>` │ `<8b>` │ 果 |
| I like eating apples | 20 | 20 | 4 | 4 | I │ ␣like │ ␣eating │ ␣apples |
| 長頸鹿 | 3 | 9 | 4 | 7 | 長 │ `<e9 a0>` │ `<b8>` │ 鹿 |
| The giraffe is eating leaves. | 29 | 29 | 7 | 7 | The │ ␣gira │ ffe │ ␣is │ ␣eating │ ␣leaves │ . |
| 長頸鹿正在吃樹葉。 | 9 | 27 | 10 | 17 | 長 │ `<e9 a0>` │ `<b8>` │ 鹿 │ 正在 │ 吃 │ `<e6 a8>` │ `<b9>` │ 葉 │ 。 |
| 😀 | 1 | 4 | 1 | 2 | 😀 |
| unbelievably | 12 | 12 | 3 | 3 | un │ bel │ ievably |

套件回報的詞彙表大小：o200k_base 是 200,006，cl100k_base 是 100,264。

## 觀察
1. 同一句話：英文「The giraffe is eating leaves.」29 個字元切成 7 個 token；中文「長頸鹿正在吃樹葉。」只有 9 個字元，卻切成 10 個 token（o200k_base），用 cl100k_base 是 17 個。
2. 新舊 tokenizer 差很多：「人工智慧」在 o200k_base 是 2 塊（人工｜智慧），在 cl100k_base 是 6 塊。
3. 中文字會被拆成「半個字」：「頸」的 3 個位元組被切成 `<e9 a0>` 和 ``<b8>`` 兩塊；cl100k_base 甚至把「鹿」拆成 3 塊、每塊 1 個位元組。
4. strawberry 被切成 st｜raw｜berry 三塊；模型看到的是三塊積木，而不是 10 個字母。
5. giraffe 前面有沒有空格，切法就不同：「giraffe」是 g｜ira｜ffe，「␣giraffe」是 ␣gira｜ffe。
6. 英文常用字多半是一整塊，而且連著前面的空格：␣like、␣eating、␣apples 各是一塊。
7. 😀 在 o200k_base 是 1 塊，在 cl100k_base 是 2 塊。

## 和其他資料的差異
- 詞彙表大小：s05（Wikipedia）寫 GPT-3.5／GPT-4 是 100,258；本實驗的套件回報 cl100k_base 是 100,264。兩者相差 6，可能是特殊 token 的算法不同，本 Wiki 尚無資料可以判斷，兩個數字並列。

## 限制
- 只測了 13 段文字和兩種 OpenAI 的編碼；其他公司模型的 tokenizer 不同，結果可能不一樣。
- 第一版程式把半個中文字算錯位置，已修正（見 `raw/experiment/README.md` 的修正紀錄）。

## 用在哪些頁面
[Token 與費用、語言](../concepts/cost-and-languages.md)、[位元組與中文](../concepts/bytes-and-chinese.md)、[看不到字母](../concepts/letters-and-spelling.md)、[詞彙表](../concepts/vocabulary.md)、[Token 不是中立的](../concepts/token-politics.md)
