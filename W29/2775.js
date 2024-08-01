let input2 = require('fs').readFileSync('js_testcase.txt').toString().split('\n').map(Number);

const board = [];
for (let i = 0; i <= 14; i++){
  let floor = [];
  for (let j = 0; j <= 14; j++){
    if (i === 0){
      floor.push(j + 1);
    }
    else if (j===0) {
      floor.push(1);
    }
    else {
      floor.push(board[i-1][j]+floor[j-1]);
    }
  }
  board.push(floor);
}
console.log(board);

for (let k = 0; k < input2[0]; k++){
  console.log(board[input2[2*k+1]][input2[2*k+2]-1])
}