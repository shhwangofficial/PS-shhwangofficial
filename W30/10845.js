const [n, ...input3] = require("fs")
  .readFileSync("js_testcase.txt")
  .toString()
  .trim()
  .split("\n");

const arr = [];
const answer = [];
for (let i = 0; i < n; i++) {
  let len = arr.length;
  let command = input3[i].trim();
  if (command === "front") {
    if (len) {
      answer.push(arr[0]);
    } else {
      answer.push(-1);
    }
  } else if (command === "back") {
    if (len) {
      answer.push(arr[len - 1]);
    } else {
      answer.push(-1);
    }
  } else if (command === "pop") {
    if (len) {
      answer.push(arr.shift());
    } else {
      answer.push(-1);
    }
  } else if (command === "size") {
    answer.push(len);
  } else if (command === "empty") {
    if (len) {
      answer.push(0);
    } else {
      answer.push(1);
    }
  } else {
    const [a, b] = command.split(" ");
    arr.push(b);
  }
}

console.log(answer.join("\n"));
