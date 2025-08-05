const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';

let input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');

let [h, m] = input[0].trim().split(' ').map(Number);
let m_inc = Number(input[1]);

m = m + m_inc;
let h_inc = Math.floor(m / 60);
m = m % 60;
h = h + h_inc;
h = h % 24;
console.log(`${h} ${m}`);
