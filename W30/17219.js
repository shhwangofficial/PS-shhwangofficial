let input = require('fs').readFileSync('js_testcase.txt').toString().split('\n');
let num = input[0].split(' ').map(Number);
let N = num[0];
let M = num[1];

object = {};
for (let i = 1; i <=N; i++){
  let line = input[i].split(' ');
  object[line[0].trim()] = line[1].trim();
}

for (let j = N+1; j <= N+M; j++){
  console.log(object[`${input[j].trim()}`]);
}

