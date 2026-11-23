---
title: openai/tiktoken README
type: source
sources: []
updated: 2026-11-23
---

# s04｜openai/tiktoken README

- 類型：開源專案說明
- 網址：https://github.com/openai/tiktoken
- 取得：2026-11-23

## 重點（用自己的話整理）
- tiktoken 是 OpenAI 模型使用的 BPE tokenizer，專案宣稱比同類開源 tokenizer 快 3–6 倍。
- 語言模型看到的是一串**數字**，不是文字；BPE 負責把文字轉成這些數字。
- BPE 的四個性質：
  1. 可逆、不失真：token 可以完整轉回原本的文字。
  2. 任何文字都能處理，包括 tokenizer 沒看過的文字。
  3. 會壓縮文字：實際上平均每個 token 約 4 個位元組。
  4. 會把常見的字根切出來，例如 encoding → encod + ing，有助於模型學到文法。
- 專案中出現的編碼名稱：`o200k_base`（主要範例）、`cl100k_base`。

## 可引用的數字
| 項目 | 數字 |
|---|---|
| 速度 | 比同類開源 tokenizer 快 3–6 倍（專案自述） |
| 平均每個 token | 約 4 個位元組 |

## 限制
- 速度數字是專案自己的測試結果。

## 用在哪些頁面
[Tokenizer](../concepts/tokenizer.md)、[Token](../concepts/token.md)
