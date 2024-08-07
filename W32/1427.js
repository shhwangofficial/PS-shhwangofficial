let N = require("fs").readFileSync("js_testcase.txt").toString().trim();
let splitted = N.split("").map(Number);
splitted.sort((a, b) => b - a);
console.log(splitted.join(""));
