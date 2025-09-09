import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())
from collections import deque

lst = []
for _ in range(N):
    lst.append(int(input()))


cnt = [0] * (d + 1)
ans = 0
add = 0
for i in range(k):
    if cnt[lst[i]] == 0:
        ans += 1
    cnt[lst[i]] += 1
if cnt[c] == 0:
    add = 1
ans += add
tmp = ans - add
i = 1
add = 0
while i < N:
    j = (i + k - 1) % N
    cnt[lst[i - 1]] -= 1
    if cnt[lst[i - 1]] == 0:
        tmp -= 1
    if cnt[lst[j]] == 0:
        tmp += 1
    cnt[lst[j]] += 1

    if cnt[c] == 0:
        add = 1

    ans = max(tmp + add, ans)
    add = 0
    i += 1

print(ans)
