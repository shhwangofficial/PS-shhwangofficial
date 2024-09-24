const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';
const input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');

let ans = [];
for (let i = 0; i < input.length; i = i + 2) {
  let N = Number(input[i].trim());
  let arr = input[i + 1].trim().split(/\s+/g).map(Number);
  let case_ans = [];

  for (let idx = 0; idx < arr.length; idx++) {
    let len = case_ans.length;

    if (!len || case_ans[len - 1] < arr[idx]) {
      case_ans.push(arr[idx]);
    } else {
      let s = 0;
      let e = len - 1;
      let temp = 0;

      while (s <= e) {
        let mid = Math.floor((s + e) / 2);
        if (case_ans[mid] >= arr[idx]) {
          temp = mid;
          e = mid - 1;
        } else {
          s = mid + 1;
        }
      }
      case_ans[temp] = arr[idx];
    }
  }
  ans.push(case_ans.length);
}

answer = '';
for (i of ans) {
  answer += i + '\n';
}

console.log(answer.trim());
