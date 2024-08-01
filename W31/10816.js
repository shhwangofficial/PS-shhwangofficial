const [N, c, M, q] = require('fs').readFileSync('BOJ/js_testcase.txt').toString().trim().split("\n");
const cards = c.split(" ").map(Number);
const querys = q.split(" ").map(Number); 
dict = {};

for (let i = 0; i<N; i++){
    if (dict[cards[i]] == undefined){
        dict[cards[i]] = 1;
    }
    else {
        dict[cards[i]] += 1;
    }
}
const ans = [];
for (let j = 0; j < M; j++){
    if (dict[querys[j]] == undefined){
        ans.push(0);
    }
    else{
        ans.push(dict[querys[j]]);
    }
}

console.log(ans.join(" "));