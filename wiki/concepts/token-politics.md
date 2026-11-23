---
title: Token 不是中立的
type: concept
sources: [s07-39c3-giraffe, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# Token 不是中立的

## 一句話
詞彙表是從大量網路資料「統計」出來的，所以哪些字能整塊保留、哪些字被拆碎，反映了資料裡誰的話比較多（s07）。

## 重點（s07）
- 品牌名稱、社群帳號、一長串驚嘆號可能是一整塊 token；一些一般的單字反而被拆成好幾塊。
- 長頸鹿（giraffe）用現有的 token 可以有 51 種拼法；有些「拼錯」的組合（g|iraffe、gir|affe）餵給生圖模型，照樣畫得出長頸鹿。
- 講者的觀點：切 token 這一步決定了什麼能被 AI 表達，因此帶有文化與商業的偏向。

## 在實際的 tokenizer 裡（s08）
- giraffe 在 o200k_base 被切成 g｜ira｜ffe，在 cl100k_base 是 g｜ir｜affe；前面加一個空格又會變成 ␣gira｜ffe。同一個字，換一個 tokenizer、多一個空格，積木就不一樣。

## 可以怎麼想
（推論）同一個意思，用英文說可能只要幾塊，用其他語言說卻要更多塊；這會讓不同語言的使用者在費用與可用長度上處在不同的起跑點（數字見 [Token 與費用、語言](cost-and-languages.md)）。

## 相關頁面
[詞彙表](vocabulary.md)、[Token](token.md)、[總覽](../overview.md)

## 依據
[s07 39C3：51 Ways to Spell the Image Giraffe](../sources/s07-39c3-giraffe.md)、[s08 自己的實驗](../sources/s08-experiment-gpt-tokenizer.md)
