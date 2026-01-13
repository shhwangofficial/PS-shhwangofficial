import sys
from itertools import combinations

N, C = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

A_lst, B_lst = num[: N // 2], num[N // 2 :]
A_sum = [0]
for i in range(1, len(A_lst) + 1):
    for j in combinations(A_lst, i):
        A_sum.append(sum(j))

B_sum = [0]
for i in range(1, len(B_lst) + 1):
    for j in combinations(B_lst, i):
        B_sum.append(sum(j))

B_sum.sort()

ans = 0
dic = {}
for i in range(len(A_sum)):
    W = A_sum[i]
    if dic.get(W, 0):
        ans += dic[W]
        continue
    for j in range(len(B_sum) - 1, -1, -1):
        if W + B_sum[j] <= C:
            ans += j + 1
            dic[W] = j + 1
            break
    else:
        continue

print(ans)
print(dic)
