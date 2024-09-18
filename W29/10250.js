const [n, ...input3] = require('fs')
  .readFileSync('js_testcase.txt')
  .toString()
  .trim()
  .split('\n');

for (let list of input3) {
  const test = list
    .trim()
    .split(' ')
    .map((num) => Number(num));
  let floor = test[2] % test[0];
  let block;
  if (floor === 0) {
    floor = test[0];
    block = test[2] / test[0];
  } else {
    block = Math.floor(test[2] / test[0]) + 1;
  }

  if (block <= 9) {
    console.log(`${floor}0${block}`);
  } else {
    console.log(`${floor}${block}`);
  }
}
