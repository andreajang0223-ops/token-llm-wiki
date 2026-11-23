---
title: 總覽：Token——LLM 怎麼讀文字
type: overview
sources: [s01-openai-tokens, s02-hf-bpe-course, s03-hf-tokenizer-summary, s04-tiktoken, s05-wikipedia-bpe, s06-sennrich-2016, s07-39c3-giraffe, s08-experiment-gpt-tokenizer]
updated: 2026-11-23
---

# 總覽：Token——LLM 怎麼讀文字

## 這個 Wiki 在回答什麼
AI（大型語言模型，LLM）看到的不是我們打的字，而是一串被切好的「積木」——token。
這個 Wiki 整理：token 是什麼、文字怎麼被切、為什麼中文和英文不一樣、這件事為什麼會影響費用與 AI 的表現。

## 三個最重要的發現
1. AI 讀的是 token 的編號，不是字母或單字（[Token](concepts/token.md)、[Tokenizer](concepts/tokenizer.md)）。
2. 切法是從資料統計出來的（BPE），常見的字整塊、少見的字拆碎（[BPE](concepts/bpe.md)）。
3. 同一句話，中文比英文用更多 token，而且會被拆成「半個字」；新的 tokenizer 改善很多（[費用與語言](concepts/cost-and-languages.md)）。

## 用這個 Wiki 做的成品
- 教學簡報的大綱：[queries/2026-11-23-slides-outline.md](queries/2026-11-23-slides-outline.md)

## 建議閱讀順序
1. [Token 是什麼](concepts/token.md)
2. [Tokenizer：文字與數字的翻譯機](concepts/tokenizer.md)
3. [Token 與費用、語言](concepts/cost-and-languages.md)
4. [上下文長度](concepts/context-window.md)
5. [三種切法](concepts/tokenization-levels.md)
6. [BPE：文字怎麼被切](concepts/bpe.md)
7. [詞彙表](concepts/vocabulary.md)
8. [位元組與中文](concepts/bytes-and-chinese.md)
9. [為什麼 AI 看不到字母](concepts/letters-and-spelling.md)
10. [Token 不是中立的](concepts/token-politics.md)
