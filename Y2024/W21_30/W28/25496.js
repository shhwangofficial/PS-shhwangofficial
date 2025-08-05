let [PN, An] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
let [P, N] = PN.split(' ').map(Number);
let A = An.split(' ').map(Number);

A.sort(function (a, b) {
  return a - b;
});

let cnt = 0;
for (const val of A) {
  if (P < 200) {
    P += val;
    cnt += 1;
  } else {
    break;
  }
}

console.log(cnt);
