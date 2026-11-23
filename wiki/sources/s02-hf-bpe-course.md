---
title: Hugging Face LLM Course：Byte-Pair Encoding tokenization
type: source
sources: []
updated: 2026-11-23
---

# s02｜Hugging Face LLM Course：Byte-Pair Encoding tokenization

- 類型：教學課程（第 6 章第 5 節）
- 網址：https://huggingface.co/learn/llm-course/chapter6/5
- 取得：2026-11-23

## 重點（用自己的話整理）
- BPE 原本是壓縮文字的方法，後來被 OpenAI 用在 GPT 的 tokenizer；GPT-2、RoBERTa、BART、DeBERTa 等模型都用它。
- **訓練（學會怎麼切）**：先把語料裡出現的所有字母當作基本詞彙；接著一再找出「最常相鄰出現的兩塊」，把它們合併成新的一塊，加入詞彙表；直到詞彙表達到想要的大小。
- **課程的小例子**：語料只有 hug（10 次）、pug（5 次）、pun（12 次）、bun（4 次）、hugs（5 次）。
  - 基本詞彙：b、g、h、n、p、s、u。
  - 第 1 次合併：u+g 一起出現 20 次最多 → 合成 `ug`。
  - 第 2 次合併：u+n 出現 16 次 → 合成 `un`。
  - 第 3 次合併：h+ug 出現 15 次 → 合成 `hug`，第一個三個字母的 token。
- **切新的文字**：照「學到的合併順序」一條一條套用。用上面三條規則：bug → `b` + `ug`；mug → `[UNK]` + `ug`，因為 m 不在基本詞彙裡（不認得的字）。
- **位元組層級的 BPE（byte-level BPE）**：GPT-2 等模型把文字當成位元組（byte）處理，基本詞彙是 256 個位元組，所以任何字元都能表示，不會出現「不認得的字」。

## 可引用的數字
| 項目 | 數字 |
|---|---|
| 例子：u+g 相鄰次數 | 20 |
| 例子：u+n 相鄰次數 | 16 |
| 例子：h+ug 相鄰次數 | 15 |
| byte-level BPE 的基本詞彙 | 256 個位元組 |

## 限制
- 例子是刻意縮小的玩具語料，真實的 tokenizer 會合併數萬次。

## 用在哪些頁面
[BPE](../concepts/bpe.md)、[位元組與中文](../concepts/bytes-and-chinese.md)
