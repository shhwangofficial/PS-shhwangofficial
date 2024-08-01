const arr1 = ["상하", "상훈", "엄마", "아빠"];

const kids = arr1.filter((member) => member[0] === "d");  // ["상하", "상훈"]

console.log(kids);