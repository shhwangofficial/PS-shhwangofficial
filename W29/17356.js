let input1 = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let [ a, b ] = input1.map(Number);

let M = (b-a) / 400;


console.log(1/(1+Math.pow(10, M)));