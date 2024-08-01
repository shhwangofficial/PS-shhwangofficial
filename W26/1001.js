let input1 = require('fs').readFileSync('js_testcase.txt').toString().split(' ');
let [ A, B ] = input1.map(num => Number(num))
console.log(A-B)