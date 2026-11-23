---
title: 為什麼 AI 看不到字母
type: concept
sources: [s08-experiment-gpt-tokenizer, s04-tiktoken]
updated: 2026-11-23
---

# 為什麼 AI 看不到字母

## 一句話
我們看到 strawberry 是 10 個字母；AI 看到的卻是 st｜raw｜berry 三塊積木的編號（s08）。

## 實驗（s08）
| 單字 | o200k_base 切成 | cl100k_base 切成 |
|---|---|---|
| strawberry | st｜raw｜berry | str｜aw｜berry |
| giraffe | g｜ira｜ffe | g｜ir｜affe |
| unbelievably | un｜bel｜ievably | un｜belie｜vably |

模型拿到的是每一塊的編號（s04），例如 strawberry 在 o200k_base 是 302、1618、19772 三個數字（s08）。

## 這代表什麼
（推論）問 AI「strawberry 裡有幾個 r」，它必須從「三個編號」推回「10 個字母」，而 r 分散在 raw 和 berry 兩塊裡，所以這類「數字母」的問題比看起來難。本 Wiki 收錄的資料沒有直接測試 AI 數字母的正確率。

## 相關頁面
[Token](token.md)、[Tokenizer](tokenizer.md)

## 依據
[s08 自己的實驗](../sources/s08-experiment-gpt-tokenizer.md)、[s04 tiktoken](../sources/s04-tiktoken.md)
