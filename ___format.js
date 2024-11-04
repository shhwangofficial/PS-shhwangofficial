// 입력을 한줄씩 받는게 아니라 한꺼번에 받는다.
// console.log 는 한번만 실행되게끔 한다.

// 필수
const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';

// N
let N = Number(require('fs').readFileSync(filePath, 'utf-8').toString().trim());

// 1 10  -> a = 1, b = 10
let input1 = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split(' ');
let [a, b] = input1.map(Number);

// 여러줄의 숫자 입력 받을 때
let input2 = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');
input2 = input2.map(Number);

// 입력값이 첫 번째 줄에는 입력 값의 길이(n), 두 번째 줄에 공백으로 구분된 입력값이 주어질 때
/* ex)
3
110 78 158
*/
const [n, input3] = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');
const inputArr3 = input3.split(' ').map(Number);

// N개의 0으로 된 일차원 배열
let dp = Array(N).fill(0);

// 이차원 배열
arr = Array.from({ length: rows }, () => Array(cols).fill(0));

// 배열 오름차순 정렬
arr.sort(function (a, b) {
  return a - b;
});
