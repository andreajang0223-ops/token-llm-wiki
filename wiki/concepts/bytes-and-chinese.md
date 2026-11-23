---
title: 位元組與中文（Byte-level BPE）
type: concept
sources: [s02-hf-bpe-course, s03-hf-tokenizer-summary, s05-wikipedia-bpe, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# 位元組與中文（Byte-level BPE）

## 一句話
GPT-2 等模型的 tokenizer 從「位元組（byte）」開始切，所以任何文字（中文、表情符號）都切得出來，不會有「不認得的字」。

## 重點
- 早期的切法如果遇到沒學過的字母，只能標成 `[UNK]`（不認得）。例如只學過 b、g、h、n、p、s、u 時，mug 的 m 就是 `[UNK]`（s02）。
- byte-level BPE 的基本詞彙是 256 個位元組，任何字元都能用位元組表示，所以不會出現 `[UNK]`（s02）。做法是先把文字轉成 UTF-8 位元組再處理（s05）。
- 中文、日文不用空格分詞，SentencePiece 這類做法直接處理原始文字、把空格也當成一個符號，所以不需要先用空格切開（s03）。

## 實際看到的「半個字」（s08）
- 一個中文字在 UTF-8 占 3 個位元組。「長頸鹿」3 個字共 9 個位元組。
- o200k_base 把「頸」拆成兩塊：前 2 個位元組 `<e9 a0>` 一塊、最後 1 個位元組 `<b8>` 一塊；單獨一塊無法顯示成字。
- cl100k_base 拆得更碎：「鹿」被拆成 3 塊，每塊 1 個位元組。
- 😀 占 4 個位元組，在 o200k_base 是 1 塊，在 cl100k_base 是 2 塊。

## 相關頁面
[BPE](bpe.md)、[Token 與費用、語言](cost-and-languages.md)

## 依據
[s02 Hugging Face BPE 課程](../sources/s02-hf-bpe-course.md)、[s03 Summary of the tokenizers](../sources/s03-hf-tokenizer-summary.md)、[s05 Wikipedia：BPE](../sources/s05-wikipedia-bpe.md)、[s08 自己的實驗](../sources/s08-experiment-gpt-tokenizer.md)
