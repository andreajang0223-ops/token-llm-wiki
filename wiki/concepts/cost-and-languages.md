---
title: Token 與費用、語言
type: concept
sources: [s01-openai-tokens, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# Token 與費用、語言

## 一句話
用 AI 的費用是「按 token 算」，而同一句話換成不同語言，切出來的 token 數不一樣。

## 重點
- 切法跟語言有關：西班牙文「Cómo estás」只有 10 個字元，卻切成 5 個 token（s01）。
- 「token 對字元的比例」較高的語言，用 API 處理同樣內容就比較貴（s01）。

## 中文 vs 英文：同一句話（s08）
| 句子 | 字元 | o200k_base | cl100k_base |
|---|---|---|---|
| The giraffe is eating leaves. | 29 | 7 tokens | 7 tokens |
| 長頸鹿正在吃樹葉。 | 9 | 10 tokens | 17 tokens |

- 中文只有 9 個字，卻比 29 個字元的英文用掉更多 token。
- 較新的 o200k_base 對中文友善很多：同一句從 17 塊降到 10 塊；「人工智慧」從 6 塊降到 2 塊。

（推論）用同一個模型處理同樣的意思，中文通常要付比英文更多的 token；換到較新的 tokenizer，差距會縮小。

## 相關頁面
[Token](token.md)、[上下文長度](context-window.md)、[位元組與中文](bytes-and-chinese.md)、[Token 不是中立的](token-politics.md)

## 依據
[s01 OpenAI：What are tokens](../sources/s01-openai-tokens.md)、[s08 自己的實驗](../sources/s08-experiment-gpt-tokenizer.md)
