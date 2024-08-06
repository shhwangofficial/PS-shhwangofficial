let input1 = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let [ a, b, c, d, e ] = input1.map(Number);
let ans = e*4 - (a+b+c+d);
if (ans < 0)
  ans = 0;
console.log(ans);