---
title: Sennrich, Haddow & Birch（2016）：Neural Machine Translation of Rare Words with Subword Units
type: source
sources: []
updated: 2026-11-23
---

# s06｜Sennrich, Haddow & Birch（2016）

- 類型：學術論文（arXiv 1508.07909，ACL 2016 接受）
- 作者：Rico Sennrich、Barry Haddow、Alexandra Birch
- 網址：https://arxiv.org/abs/1508.07909
- 取得：2026-11-23（只讀摘要）

## 重點（用自己的話整理）
- 問題：翻譯模型的詞彙表是固定的，但真實文章裡一定會出現沒看過的字（人名、複合字、外來語）。過去的做法是查字典補救。
- 解法：把少見或沒看過的字拆成「子詞」序列，讓模型可以處理開放的詞彙。論文比較了幾種切法，包括把 BPE 這個壓縮方法拿來切字。
- 結果：在 WMT 15 英德、英俄翻譯任務上，子詞模型比查字典的做法分別高 1.1 與 1.3 BLEU（翻譯品質分數）。

## 可引用的數字
| 項目 | 數字 |
|---|---|
| 英→德 改善 | +1.1 BLEU |
| 英→俄 改善 | +1.3 BLEU |

## 限制
- 只讀了摘要，沒有讀全文的實驗細節。

## 用在哪些頁面
[BPE](../concepts/bpe.md)、[三種切法](../concepts/tokenization-levels.md)
