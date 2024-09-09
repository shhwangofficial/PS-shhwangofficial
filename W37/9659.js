let N = Number(require("fs").readFileSync("/dev/stdin").toString().trim());
if (N % 2 == 1) {
  console.log("SK");
} else {
  console.log("CY");
}
