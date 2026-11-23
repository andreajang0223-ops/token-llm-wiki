// 逐 token 取得「原始位元組」，避免 decode() 的串流狀態造成錯誤歸屬
const encs = { o200k_base: require('gpt-tokenizer/encoding/o200k_base'), cl100k_base: require('gpt-tokenizer/encoding/cl100k_base') };
const samples = ['Hello world','tokenization','strawberry','giraffe',' giraffe','人工智慧','我喜歡吃蘋果','I like eating apples','長頸鹿','The giraffe is eating leaves.','長頸鹿正在吃樹葉。','😀','unbelievably'];
function bytesOf(enc, t) {
  const b = enc.default.bytePairEncodingCoreProcessor.tryDecodeToken(t);
  return typeof b === 'string' ? Buffer.from(b, 'utf8') : Buffer.from(b);
}
function label(buf) {
  const s = buf.toString('utf8');
  return s.includes('�') ? '<' + [...buf].map(x => x.toString(16).padStart(2, '0')).join(' ') + '>' : s;
}
for (const s of samples) {
  const row = { text: s, chars: [...s].length, bytes: Buffer.byteLength(s, 'utf8') };
  for (const [n, e] of Object.entries(encs)) {
    const ids = e.encode(s);
    row[n] = { count: ids.length, ids, pieces: ids.map(t => label(bytesOf(e, t))) };
  }
  console.log(JSON.stringify(row));
}
console.error('vocabularySize', encs.o200k_base.vocabularySize, encs.cl100k_base.vocabularySize);
