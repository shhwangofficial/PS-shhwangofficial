const [N, input3] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const nums = input3.trim().split(' ');

for (let i = 0; i < nums.length; i++) {
  nums[i] = Number(nums[i]);
}
nums.sort(function (a, b) {
  return a - b;
});
let sum_ = 0;
let digit = Number(N);
for (let i = 0; i < nums.length; i++) {
  sum_ += nums[i] * digit;
  digit -= 1;
}

console.log(sum_);
