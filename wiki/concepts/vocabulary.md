---
title: 詞彙表（Vocabulary）
type: concept
sources: [s03-hf-tokenizer-summary, s05-wikipedia-bpe, s07-39c3-giraffe, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# 詞彙表（Vocabulary）

## 一句話
詞彙表是 tokenizer 的「積木目錄」：列出所有可以用的 token，每塊都有一個編號，模型實際看到的就是這些編號。

## 有多大（s03、s05）
| 模型 | 詞彙表大小 | 組成 |
|---|---|---|
| GPT | 40,478 | 478 個基本符號 + 40,000 次合併 |
| GPT-2 | 50,257 | 256 個位元組 + 50,000 次合併 + 1 個結束符號 |
| GPT-3.5、GPT-4 | 100,258 | 100,000 個 BPE token + 258 個特殊 token（s05） |
| cl100k_base（套件回報） | 100,264 | 本 Wiki 的實驗套件數字（s08） |
| o200k_base（套件回報） | 200,006 | 本 Wiki 的實驗套件數字（s08） |

資料不一致：s05 寫 100,258、s08 的套件回報 100,264，相差 6，可能是特殊 token 的算法不同，本 Wiki 尚無資料可以判斷。

BPE 的詞彙表大小 = 基本詞彙數 + 合併次數（s03）。

詞彙表是依訓練資料的出現頻率統計出來的，所以它反映了資料的組成（s07，見 [Token 不是中立的](token-politics.md)）。

詞彙表較大的 o200k_base（200,006）切中文比 cl100k_base（100,264）省很多：「長頸鹿正在吃樹葉。」從 17 塊降到 10 塊（s08）。這支持「詞彙表越大，同一段文字切出的 token 越少」，但只測了少數句子，仍屬（推論）。

## 相關頁面
[BPE](bpe.md)、[三種切法](tokenization-levels.md)

## 依據
[s03 Hugging Face：Summary of the tokenizers](../sources/s03-hf-tokenizer-summary.md)、[s05 Wikipedia：BPE](../sources/s05-wikipedia-bpe.md)、[s07 39C3 演講](../sources/s07-39c3-giraffe.md)、[s08 自己的實驗](../sources/s08-experiment-gpt-tokenizer.md)
