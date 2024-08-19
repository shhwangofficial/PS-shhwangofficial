import sys
from collections import defaultdict
import heapq

N, M = map(int, sys.stdin.readline().split())
dic = defaultdict(int)
for i in range(N + M):
    fr, to = map(int, sys.stdin.readline().split())
    dic[fr] = to

inf = 99999
min_steps = [inf] * 101
min_steps[1] = 0
heap = [(0, 1)]
while heap:
    steps, now = heapq.heappop(heap)
    if now == 100:
        print(steps)
        break
    for i in range(1, 7):
        dest = dic[now + i]
        if dest:
            if min_steps[dest] > steps + 1:
                min_steps[dest] = steps + 1
                heapq.heappush(heap, (steps + 1, dest))
        else:
            if 0 < now + i <= 100 and min_steps[now + i] > steps + 1:
                min_steps[now + i] = steps + 1
                heapq.heappush(heap, (steps + 1, now + i))
