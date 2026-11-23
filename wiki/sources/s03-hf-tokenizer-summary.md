---
title: Hugging Face Transformers：Summary of the tokenizers
type: source
sources: []
updated: 2026-11-23
---

# s03｜Hugging Face Transformers：Summary of the tokenizers

- 類型：技術文件
- 網址：https://huggingface.co/docs/transformers/tokenizer_summary
- 取得：2026-11-23

## 重點（用自己的話整理）
- **以「整個單字」為單位**：love、loving、loved、lovingly 都要各占一格，詞彙表會非常大，佔用很多記憶體與運算；沒看過的字只能變成 `<unk>`。
- **以「單一字元」為單位**：詞彙表很小、什麼字都能表示，但句子變得很長，而且單一字母（例如 l）攜帶的意義遠少於 love，模型表現較差。
- **子詞（subword）**：折衷做法。常見的字保留成一整塊，少見的字拆成有意義的小塊，例如 annoyingly 可能被拆成 annoying + ly，或 annoy + ing + ly，取決於詞彙表。
- 常見的子詞演算法：
  - BPE：從字元開始，一再合併最常相鄰的一對（Llama、Gemma、Qwen2、GPT、GPT-2 等使用）。
  - WordPiece：和 BPE 類似，但挑「最能提高訓練資料機率」的一對合併（BERT 家族，如 DistilBERT、Electra）。
  - Unigram：從很大的候選集合開始，一再刪掉影響最小的 token（T5 等使用）。
  - SentencePiece：直接處理原始文字、把空格也當成符號 `▁`，適合中文、日文這類不用空格分詞的語言。
- 詞彙表大小：GPT 是 40,478（478 個基本符號＋40,000 次合併）；GPT-2 是 50,257（256 個位元組＋50,000 次合併＋1 個結束符號）。BPE 的詞彙表大小 = 基本詞彙數 + 合併次數。

## 可引用的數字
| 項目 | 數字 |
|---|---|
| GPT 詞彙表 | 40,478 = 478 + 40,000 |
| GPT-2 詞彙表 | 50,257 = 256 + 50,000 + 1 |

## 限制
- 文件說明演算法原理，沒有比較各語言實際的 token 數。

## 用在哪些頁面
[三種切法](../concepts/tokenization-levels.md)、[詞彙表](../concepts/vocabulary.md)、[BPE](../concepts/bpe.md)、[位元組與中文](../concepts/bytes-and-chinese.md)
