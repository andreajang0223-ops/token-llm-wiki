---
title: 上下文長度（Context Window）
type: concept
sources: [s01-openai-tokens]
updated: 2026-11-23
---

# 上下文長度（Context Window）

## 一句話
AI 一次能「看見」的內容有上限，這個上限是用 token 數計算的，而且你的提問和 AI 的回答共用同一個額度。

## 例子
- 早期的模型，提問加上回答最多共 2048 個 token（s01）。新模型的上限已經大很多，但本 Wiki 尚無各模型最新上限的資料。
- 用 s01 的經驗法則換算，2048 個 token 大約是 1,500 個英文單字。

## 白話比喻
（推論）像一張固定大小的白板：題目寫得越長，留給 AI 寫答案的空間就越少；用 token 越多的語言，同一張白板能寫的內容就越少。

## 相關頁面
[Token](token.md)、[Token 與費用、語言](cost-and-languages.md)

## 依據
[s01 OpenAI：What are tokens](../sources/s01-openai-tokens.md)
