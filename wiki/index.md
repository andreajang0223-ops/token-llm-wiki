# Token LLM Wiki｜目錄

主題：Token——LLM 怎麼讀文字。讀者：完全沒接觸過 AI 的人。
從 [總覽](overview.md) 開始讀。工作規則見 repo 根目錄的 AGENTS.md，工作紀錄見 [log](log.md)。

## 總覽
- [overview.md](overview.md)｜整個主題的地圖與建議閱讀順序

## 概念
- [concepts/token.md](concepts/token.md)｜Token 是什麼：AI 讀文字用的積木
- [concepts/tokenizer.md](concepts/tokenizer.md)｜Tokenizer：把文字換成編號、再換回文字
- [concepts/cost-and-languages.md](concepts/cost-and-languages.md)｜費用按 token 算，不同語言切出的 token 數不同
- [concepts/context-window.md](concepts/context-window.md)｜AI 一次能看見的內容上限，以 token 計
- [concepts/tokenization-levels.md](concepts/tokenization-levels.md)｜整個詞、單一字元、子詞三種切法的取捨
- [concepts/vocabulary.md](concepts/vocabulary.md)｜詞彙表：所有 token 的目錄與大小
- [concepts/bpe.md](concepts/bpe.md)｜BPE：一再合併最常一起出現的兩塊
- [concepts/letters-and-spelling.md](concepts/letters-and-spelling.md)｜AI 看到的是積木不是字母：strawberry = st｜raw｜berry
- [concepts/token-politics.md](concepts/token-politics.md)｜詞彙表反映資料組成，切法不是中立的
- [concepts/bytes-and-chinese.md](concepts/bytes-and-chinese.md)｜從位元組開始切，任何文字都切得出來

## 資料來源
- [sources/s01-openai-tokens.md](sources/s01-openai-tokens.md)｜OpenAI 官方說明：token 的定義與經驗法則
- [sources/s02-hf-bpe-course.md](sources/s02-hf-bpe-course.md)｜Hugging Face 課程：BPE 的訓練與 hug/pug 例子
- [sources/s03-hf-tokenizer-summary.md](sources/s03-hf-tokenizer-summary.md)｜Hugging Face 文件：三種切法、各種子詞演算法、詞彙表大小
- [sources/s04-tiktoken.md](sources/s04-tiktoken.md)｜tiktoken：模型看到的是數字、BPE 的四個性質
- [sources/s05-wikipedia-bpe.md](sources/s05-wikipedia-bpe.md)｜維基百科：BPE 起源（1994 壓縮法）、GPT-4 詞彙表大小
- [sources/s06-sennrich-2016.md](sources/s06-sennrich-2016.md)｜Sennrich 2016 論文：用子詞解決翻譯的罕見字問題
- [sources/s07-39c3-giraffe.md](sources/s07-39c3-giraffe.md)｜39C3 演講：長頸鹿的 51 種拼法與 token 語言的政治
- [sources/s08-experiment-gpt-tokenizer.md](sources/s08-experiment-gpt-tokenizer.md)｜自己的實驗：兩種 tokenizer 切 13 段中英文
