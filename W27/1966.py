import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    n, idx = map(int,sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    nums = deque([])
    for i in range(n):
        nums.append(i)
    cnt = 1
    while nums:
        now = nums.popleft()
        if importance[now] < max(importance):
            nums.append(now)
        else:
            if now == idx:
                print(cnt)
                break
            else:
                cnt += 1
                importance[now] = 0
