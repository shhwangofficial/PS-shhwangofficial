let input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');
let [N, ...names] = input;
N = parseInt(N);
names = names.map((name) => name.trim());
const dic = {};

for (let i = 0; i < N; i++) {
  if (dic[names[i]]) {
    dic[names[i]]++;
  } else {
    dic[names[i]] = 1;
  }
}

for (let j = N; j < 2 * N - 1; j++) {
  dic[names[j]]--;
}

for (key in dic) {
  if (dic[key] >= 1) {
    console.log(key);
    break;
  }
}
