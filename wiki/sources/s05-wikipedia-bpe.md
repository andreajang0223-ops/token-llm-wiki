---
title: Wikipedia：Byte-pair encoding
type: source
sources: []
updated: 2026-11-23
---

# s05｜Wikipedia：Byte-pair encoding

- 類型：百科條目
- 網址：https://en.wikipedia.org/wiki/Byte-pair_encoding
- 取得：2026-11-23

## 重點（用自己的話整理）
- 起源：Philip Gage 在 1994 年提出，原本是**資料壓縮**方法：一再把最常出現的一對位元組換成一個沒用過的符號，並用對照表還原。
- 壓縮小例子：`aaabdaaabac`
  - aa 最常出現 → 換成 Z：`ZabdZabac`
  - ab 換成 Y：`ZYdZYac`
  - ZY 還可以換成 X：`XdXac`，無法再壓縮。解壓縮時照相反順序換回來。
- 語言模型用的是修改版：目的不是壓到最小，而是從單一字元開始合併，直到詞彙表達到設定的大小，把文字切成一串編號。
- byte-level BPE 先把文字轉成 UTF-8 位元組再處理，所以任何 UTF-8 文字都能編碼，不需要「不認得」符號；RoBERTa、BART、DeBERTa、GPT-2 使用。
- 詞彙表大小：GPT-3.5 與 GPT-4 是 100,258（100,000 個 BPE token ＋ 258 個特殊 token）。

## 可引用的數字
| 項目 | 數字 |
|---|---|
| 提出年份 | 1994（Philip Gage） |
| GPT-3.5／GPT-4 詞彙表 | 100,258 = 100,000 + 258 |

## 限制
- 條目沒有討論不同語言的 token 數差異。

## 用在哪些頁面
[BPE](../concepts/bpe.md)、[詞彙表](../concepts/vocabulary.md)、[位元組與中文](../concepts/bytes-and-chinese.md)
