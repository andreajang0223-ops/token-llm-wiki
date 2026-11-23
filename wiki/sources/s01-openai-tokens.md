---
title: OpenAI：What are tokens and how to count them?
type: source
sources: []
updated: 2026-11-23
---

# s01｜OpenAI：What are tokens and how to count them?

- 類型：官方說明（OpenAI Help Center）
- 網址：https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- 取得：2026-11-23

## 重點（用自己的話整理）
- Token 是「字的片段」。文字送進模型前會先被切成 token，切的位置不一定在兩個單字中間，token 也可能包含前面的空格或只是半個單字。
- 英文的經驗法則：1 個 token 約 4 個字元，約 ¾ 個英文單字；100 個 token 約 75 個英文單字；1,500 個英文單字約 2048 個 token。
- 切法跟語言有關：西班牙文「Cómo estás」10 個字元就切成 5 個 token。非英文的「token 對字元比例」較高，用 API 就比較貴。
- 早期模型的上限以 token 計算：提問加回答共用最多 2048 個 token。
- OpenAI 提供互動式的 Tokenizer 工具，可以看到文字被切成哪些 token。
- 每個 token 都有編號：例如 ` egg` 是 5935、` eggs` 是 9653（可以用 `logit_bias` 參數調高或調低某個 token 出現的機率）。

## 可引用的數字
| 項目 | 數字 |
|---|---|
| 1 token ≈ | 4 個英文字元、¾ 個英文單字 |
| 100 tokens ≈ | 75 個英文單字 |
| 1,500 個英文單字 ≈ | 2048 tokens |
| 「Cómo estás」 | 10 個字元 → 5 tokens |
| 早期模型上限 | 提問＋回答共 2048 tokens |

## 限制
- 這篇說明的例子與上限屬於較早期的模型（文中提到 davinci、ada），新模型的上限與 tokenizer 已不同；本 Wiki 只把 2048 當作「上限以 token 計」的例子。
- 文中沒有中文的例子，中文的數字見 [s08 自己的實驗](s08-experiment-gpt-tokenizer.md)。

## 用在哪些頁面
[Token](../concepts/token.md)、[Token 與費用、語言](../concepts/cost-and-languages.md)、[上下文長度](../concepts/context-window.md)
