let input = require("fs").readFileSync("js_testcase.txt").toString().split(" ");
let num = Number(input);
let i = 1;
let string = "";
for (i; i <= num; i++) {
  string += i + "\n";
}

console.log(string);
