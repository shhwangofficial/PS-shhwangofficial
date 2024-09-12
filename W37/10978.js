let input = require("fs")
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split("\n");

let T = parseInt(input[0]); // 첫 번째 줄: 테스트 케이스 개수
const ans = [];

for (let i = 1; i <= T; i++) {
  let N = BigInt(input[i]); // 각 테스트 케이스의 N 값을 BigInt로 변환

  if (N === 1n) {
    ans.push(0);
  } else {
    let a = 0n,
      b = 1n;

    for (let j = 3n; j <= N; j++) {
      [a, b] = [b, (j - 1n) * (a + b)];
    }
    ans.push(b);
  }
}
console.log(ans.join("\n"));