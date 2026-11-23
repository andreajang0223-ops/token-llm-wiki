---
title: 提問：給完全沒接觸過 AI 的人，10 分鐘的 Token 教學簡報要怎麼排？
type: query
sources: [s01-openai-tokens, s02-hf-bpe-course, s03-hf-tokenizer-summary, s05-wikipedia-bpe, s06-sennrich-2016, s07-39c3-giraffe, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# 提問：Token 教學簡報的大綱

## 問題
讀者是完全沒接觸過 AI 的人，簡報約 12 頁、10 分鐘。從這個 Wiki 能排出什麼樣的大綱？每一頁要依據哪些 Wiki 頁？

## 查詢過程
1. 讀 [index](../index.md) 與 [總覽](../overview.md)，以「三個最重要的發現」作為簡報主線。
2. 依讀者程度挑頁：用 [為什麼 AI 看不到字母](../concepts/letters-and-spelling.md) 的 strawberry 當開場；BPE 只用 [BPE](../concepts/bpe.md) 的 hug 小例子，不講 WordPiece、Unigram。
3. 中文讀者最有感的是 [Token 與費用、語言](../concepts/cost-and-languages.md) 與 [位元組與中文](../concepts/bytes-and-chinese.md) 的實驗數字，放在中段。
4. 結尾用 [Token 不是中立的](../concepts/token-politics.md) 拉高到「為什麼值得在意」。

## 大綱（每頁一件事）
| # | 這頁要說的一句話 | 依據的 Wiki 頁 |
|---|---|---|
| 1 | 封面：AI 怎麼「讀」文字？ | overview |
| 2 | AI 看到的 strawberry 不是 10 個字母，而是 3 塊積木 | concepts/letters-and-spelling |
| 3 | 文字會先被切成積木，這些積木叫 token | concepts/token |
| 4 | 積木會換成編號，AI 只看得到數字 | concepts/token、concepts/tokenizer |
| 5 | 切法有三種，現在用「常見片段」 | concepts/tokenization-levels |
| 6 | BPE：一再把最常一起出現的兩塊黏起來 | concepts/bpe |
| 7 | 這個方法原本是拿來壓縮檔案的 | concepts/bpe |
| 8 | 同一句話，中文用掉的 token 比英文多 | concepts/cost-and-languages |
| 9 | 一個中文字甚至會被切成兩半 | concepts/bytes-and-chinese |
| 10 | 費用與「一次能讀多長」都用 token 計算 | concepts/cost-and-languages、concepts/context-window |
| 11 | Token 不是中立的：長頸鹿有 51 種拼法 | concepts/token-politics |
| 12 | 三個重點與自己動手試 | overview |

## 檢查大綱
- 12 頁都找得到依據的 Wiki 頁：通過。
- 第 2 頁「AI 數不清字母」在 Wiki 裡是（推論），簡報上必須照樣標示為推測，不可說成已證實。
- 第 10 頁不能寫各模型最新的上下文長度：Wiki 尚無資料，只講「用 token 計算」的概念。
- 沒有需要回到 Ingest 補資料的頁面。
