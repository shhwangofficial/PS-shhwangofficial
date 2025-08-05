import sys
from collections import defaultdict

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dic = defaultdict(int)
for num in nums:
    dic[num] += 1

stack = []
ans = [0] * N
for idx, num in enumerate(nums):
    while 1:
        if not stack or dic[num] <= dic[stack[-1][1]]:
            stack.append((idx, num))
            break
        else:
            ans[stack[-1][0]] = num
            stack.pop()

while stack:
    idx, num = stack.pop()
    ans[idx] = -1

print(*ans)
