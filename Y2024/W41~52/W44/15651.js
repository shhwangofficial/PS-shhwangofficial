const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';

let input1 = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split(' ');
let [N, M] = input1.map(Number);

let ans = '';
let lst = [];
const solve = (len) => {
  if (len === M) {
    ans += lst.join(' ') + '\n';
    return;
  }

  for (let i = 1; i <= N; i++) {
    lst.push(i);
    solve(len + 1);
    lst.pop();
  }
};

solve(0);
console.log(ans.trim());
