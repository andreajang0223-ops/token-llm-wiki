---
title: Tokenizer（切詞器）：文字 → 數字 → 文字
type: concept
sources: [s04-tiktoken]
updated: 2026-11-23
---

# Tokenizer（切詞器）

## 一句話
Tokenizer 是 AI 前面的「翻譯機」：把文字切成 token、換成編號交給模型；模型回答的編號，再由它轉回文字。

## 流程
```
你打的字 → tokenizer 切塊 → 一串編號 → 模型 → 一串編號 → tokenizer 還原 → 你看到的回答
```

## 重點（s04）
- 模型看到的是數字，不是文字。
- 轉換可逆、不失真：編號可以完整還原成原本的文字。
- 沒看過的文字也能處理。
- 平均每個 token 約 4 個位元組，所以 token 也是一種壓縮。
- 不同的模型用不同的 tokenizer，例如 `o200k_base`、`cl100k_base` 這兩種編碼。

## 相關頁面
[Token](token.md)、[BPE](bpe.md)、[詞彙表](vocabulary.md)

## 依據
[s04 openai/tiktoken](../sources/s04-tiktoken.md)
