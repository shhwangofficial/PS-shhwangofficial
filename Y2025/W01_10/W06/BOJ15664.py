import sys

N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
ans = [0]


def backtrack(lst, index):
    if len(lst) == M and lst not in ans:
        ans.append(lst)
        return
    for i in range(index, N):
        backtrack(lst + [nums[i]], i + 1)


backtrack([], 0)

for a in ans[1:]:
    print(*a)
