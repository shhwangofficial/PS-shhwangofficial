const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';
let N = Number(require('fs').readFileSync(filePath, 'utf-8').toString().trim());

N = N / 3;

const solve = (n, temp) => {
  if (n == 1) {
    temp = ['  *  ', ' * * ', '*****'];
  }
  if (n == N) {
    return temp;
  } else {
    let blanks = ' '.repeat(n * 3);
    let top = temp.map((e) => blanks + e + blanks);
    let bottom = temp.map((e) => e + ' ' + e);
    temp = [...top, ...bottom];
    return solve(n * 2, temp);
  }
};

console.log(solve(1, []).join('\n'));
