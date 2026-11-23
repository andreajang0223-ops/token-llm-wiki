---
title: Token（詞元）
type: concept
sources: [s01-openai-tokens, s04-tiktoken, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# Token（詞元）

## 一句話
Token 是 AI 讀文字時用的「積木」：文字會先被切成一塊一塊的 token，模型處理的是這些積木，而不是一個一個字母或單字。

## 為什麼要知道
- AI 計費、可以讀多長的文章，都是用 token 數計算（見 [Token 與費用、語言](cost-and-languages.md)、[上下文長度](context-window.md)）。
- AI 有些奇怪的錯誤，例如數不清單字裡有幾個字母，可能和 token 的切法有關（見 [為什麼 AI 看不到字母](letters-and-spelling.md)）。

## 例子
- token 不一定是完整的單字：可能是半個單字，也可能連著前面的空格（s01）。
- 英文經驗法則：1 個 token 約 4 個字元、約 ¾ 個單字；100 個 token 約 75 個英文單字（s01）。
- 模型真正看到的是 token 的**編號**（一串數字），由 [tokenizer](tokenizer.md) 負責轉換（s04）。
- 常見的字根會被切出來，例如 encoding → encod + ing（s04）。
- 實際切切看：Hello world 是 2 個 token，編號 13225、2375（o200k_base，s08）。

## 相關頁面
[總覽](../overview.md)、[三種切法](tokenization-levels.md)、[BPE：怎麼切](bpe.md)、[詞彙表](vocabulary.md)

## 依據
[s01 OpenAI：What are tokens](../sources/s01-openai-tokens.md)、[s04 tiktoken](../sources/s04-tiktoken.md)、[s08 自己的實驗](../sources/s08-experiment-gpt-tokenizer.md)
