import sys

from collections import deque

N, L = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

deq = deque([])
for idx, num in enumerate(nums):
    if not deq:
        deq.append([idx, num])
    else:
        if idx >= deq[0][0] + L:
            deq.popleft()
        while 1:
            if not deq:
                break
            if deq[-1][1] > num:
                deq.pop()
                continue
            else:
                break
        deq.append([idx, num])
    print(deq[0][1], end=" ")
