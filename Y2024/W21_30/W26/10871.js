let input = require('fs')
  .readFileSync('js_testcase.txt')
  .toString()
  .split('\n');
let [N, X] = input[0].split(' ').map(Number);
let num = input[1].split(' ');

let ans = '';

for (let i = 0; i < N; i++) {
  if (Number(num[i]) < X) ans += num[i] + ' ';
}

console.log(ans);
