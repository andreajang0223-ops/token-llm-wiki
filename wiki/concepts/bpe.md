---
title: BPE（Byte-Pair Encoding，位元組對編碼）
type: concept
sources: [s02-hf-bpe-course, s03-hf-tokenizer-summary, s05-wikipedia-bpe, s06-sennrich-2016]
updated: 2026-11-23
---

# BPE（Byte-Pair Encoding）

## 一句話
BPE 是決定「文字要怎麼切成 token」最常見的方法：從單一字母開始，一再把**最常黏在一起出現的兩塊**合併成一塊。

## 白話比喻
（推論）像整理樂高：先全部拆成最小的顆粒，再看哪兩顆最常被一起用，就把它們黏成一個固定零件；黏了很多次之後，常見的單字會變成一整塊，罕見的單字還是由小塊拼成。

## 小例子（s02）
語料：hug ×10、pug ×5、pun ×12、bun ×4、hugs ×5

| 步驟 | 合併 | 為什麼 |
|---|---|---|
| 一開始 | b、g、h、n、p、s、u | 所有出現過的字母 |
| 第 1 次 | u + g → `ug` | 相鄰出現 20 次，最多 |
| 第 2 次 | u + n → `un` | 相鄰出現 16 次 |
| 第 3 次 | h + ug → `hug` | 相鄰出現 15 次 |

學會這三條規則後，切新字時照順序套用：bug → `b` + `ug`。

## 從哪裡來
| 年份 | 事件 |
|---|---|
| 1994 | Philip Gage 提出 BPE，原本是**壓縮資料**的方法（s05） |
| 2016 | Sennrich 等人把 BPE 拿來切字，讓翻譯模型能處理沒看過的字，英德、英俄翻譯分別進步 1.1 與 1.3 BLEU（s06） |
| 之後 | GPT 系列等語言模型都用 BPE 切 token（s02、s03） |

壓縮版的小例子（s05）：`aaabdaaabac` → aa 換成 Z → ab 換成 Y → ZY 換成 X → `XdXac`。
語言模型的版本不追求壓到最小，而是合併到詞彙表達到設定大小就停（s05）。

## 誰在用（s03）
Llama、Gemma、Qwen2、GPT、GPT-2 等模型使用 BPE。其他做法還有 WordPiece（BERT 家族）與 Unigram（T5 等），原理不同但目的相同：決定怎麼把文字切成子詞。

## 相關頁面
[Token](token.md)、[三種切法](tokenization-levels.md)、[詞彙表](vocabulary.md)、[位元組與中文](bytes-and-chinese.md)、[總覽](../overview.md)

## 依據
[s02 Hugging Face BPE 課程](../sources/s02-hf-bpe-course.md)、[s03 Summary of the tokenizers](../sources/s03-hf-tokenizer-summary.md)、[s05 Wikipedia：BPE](../sources/s05-wikipedia-bpe.md)、[s06 Sennrich 2016](../sources/s06-sennrich-2016.md)
