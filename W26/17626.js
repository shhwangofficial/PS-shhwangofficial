// 'js_testcase.txt'
// /dev/stdin
let input = require('fs').readFileSync('/dev/stdin').toString()
let N = Number(input);

let dp = Array(N + 1).fill(0);
let squares = []

for (let i = 1; i <= Math.floor(Math.sqrt(N)); i++) {
  let j = i ** 2
  dp[j] = 1
  squares.push(j)
}

for (let i = 2; i <= N; i++) {
  let min_ = 999999
  for (let square of squares) {
    if (i - square < 0) {
      break
    }
    else if (i - square == 0) {
      min_ = 0
      break
    }
    else {
      if (dp[i - square] < min_) {
        min_ = dp[i - square]
      }
    }
  }
  dp[i] = min_ + 1
}

console.log(dp[dp.length - 1])