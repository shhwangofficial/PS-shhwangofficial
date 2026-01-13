const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';

let N = Number(require('fs').readFileSync(filePath, 'utf-8').toString().trim());

const arr = Array.from({ length: N + 1 }, () => Array(6).fill(0));

arr[1] = [1, 1, 0, 1, 0, 0];

let [O, A, AA, L, LA, LAA] = [0, 1, 2, 3, 4, 5];
let mod = 1000000;

for (let i = 2; i <= N; i++) {
  let [o, a, aa, l, la, laa] = arr[i - 1];
  arr[i][O] += (o + a + aa) % mod;
  arr[i][A] += o % mod;
  arr[i][AA] += a % mod;
  arr[i][L] += (o + a + aa + l + la + laa) % mod;
  arr[i][LA] += l % mod;
  arr[i][LAA] += la % mod;
}
ans = 0;
arr[N].forEach((e) => (ans = ans + e));
console.log(ans % mod);
