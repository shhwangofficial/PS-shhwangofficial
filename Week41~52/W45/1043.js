const filePath = process.platform === 'linux' ? 0 : 'js_testcase.txt';

let input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n')
  .map((lst) =>
    lst
      .trim()
      .split(' ')
      .map((el) => Number(el))
  );

let [nm, truth, ...parties] = input;
let [n, m] = nm;
let [knowsTruthLen, ...knowsTruth] = truth;

let parent = [...Array(n + 1)].map((_, i) => i); // 초기에는 각자가 자기 자신을 부모로 가짐
let rank = Array(n + 1).fill(1); // 트리의 높이를 기록하는 배열

// Find 함수에 경로 압축을 적용
function find(x) {
  if (parent[x] !== x) {
    parent[x] = find(parent[x]); // 경로 압축
  }
  return parent[x];
}

// Union 함수에 랭크 기반 합치기를 적용
function union(x, y) {
  let rootX = find(x);
  let rootY = find(y);

  if (rootX !== rootY) {
    // 랭크를 비교하여 작은 트리를 큰 트리에 연결
    if (rank[rootX] > rank[rootY]) {
      parent[rootY] = rootX;
    } else if (rank[rootX] < rank[rootY]) {
      parent[rootX] = rootY;
    } else {
      parent[rootY] = rootX;
      rank[rootX] += 1; // 높이가 같다면 하나의 트리의 랭크를 증가
    }
  }
}

// 각 파티의 멤버들을 같은 그룹으로 연결
for (let party of parties) {
  let [partyLen, ...partyMembers] = party;
  for (let i = 1; i < partyLen; i++) {
    union(partyMembers[0], partyMembers[i]);
  }
}

// 진실을 아는 사람들의 그룹을 찾아 표시
const truthGroups = knowsTruth.map(find);

// 거짓말을 할 수 있는 파티의 수 계산
let ans = m;
for (let party of parties) {
  const partyLeader = find(party[1]); // 파티 멤버 중 하나의 대표를 찾음
  if (truthGroups.some((truthLeader) => truthLeader === partyLeader)) {
    ans -= 1; // 진실을 아는 그룹에 속한 경우 거짓말 불가
  }
}

console.log(ans);
