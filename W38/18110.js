const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';
let input = require("fs")
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split("\n");

let [len, ...op] = input;
len = Number(len);

if (len === 0) {
  console.log(0);
} else {
  op = op.map((a) => Number(a));
  op.sort(function (a, b) {
    return a - b;
  });

  let edge = Math.round(len * 0.15);

  op = op.slice(edge, op.length - edge);
  let sum = op.reduce((acc, val) => acc + val, 0);

  console.log(Math.round(sum / (len - edge * 2)));
}
