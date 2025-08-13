import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict

N, M = map(int, input().split())
dic = defaultdict(int)
for _ in range(N):
    dic[input()] += 1
K = int(input())
ans = 0
for row in dic.keys():
    tmp = 0
    for i in range(M):
        if row[i] == "0":
            tmp += 1
    if tmp <= K:
        if (K - tmp) % 2 == 0:
            ans = max(ans, dic[row])
print(ans)
