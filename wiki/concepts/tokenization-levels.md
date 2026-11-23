---
title: 三種切法：整個詞、單一字元、子詞
type: concept
sources: [s03-hf-tokenizer-summary, s06-sennrich-2016]
updated: 2026-11-23
---

# 三種切法：整個詞、單一字元、子詞

## 一句話
把文字切成 token 有三種思路，本 Wiki 收錄的模型（GPT 系列、Llama、BERT、T5 等）都用中間路線「子詞（subword）」：常見的字整塊保留，少見的字拆成小塊。

## 比較（s03）
| 切法 | 好處 | 壞處 |
|---|---|---|
| 整個詞 | 每塊都有完整意義 | 詞彙表太大（love、loving、loved、lovingly 各一格）；沒看過的字無法處理 |
| 單一字元 | 詞彙表很小，什麼都能表示 | 句子變很長，單一字母幾乎沒有意義 |
| 子詞 | 兩者折衷 | 切的位置不一定符合人的直覺 |

## 例子
- annoyingly → annoying + ly，或 annoy + ing + ly（看詞彙表而定）（s03）。
- 子詞的想法在 2016 年被用來解決翻譯模型「沒看過的字」的問題：人名、複合字、外來語都可以拆成小塊處理（s06）。

## 相關頁面
[Token](token.md)、[BPE](bpe.md)、[詞彙表](vocabulary.md)

## 依據
[s03 Hugging Face：Summary of the tokenizers](../sources/s03-hf-tokenizer-summary.md)、[s06 Sennrich 2016](../sources/s06-sennrich-2016.md)
