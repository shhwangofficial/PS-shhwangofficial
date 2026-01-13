import sys

N, L = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))
num.sort()


lst = [0] * 1001
for i in num:
    lst[i] = 1

ans = 0
for i in range(1001):
    if lst[i] == 1:
        ans += 1
        for j in range(i, min(1001, i + L)):
            lst[j] = 0

print(ans)
