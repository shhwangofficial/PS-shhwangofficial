import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq
from collections import defaultdict

N, P, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(P):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

largest = [[float("inf")] * (N + 1) for _ in range(K + 1)]
largest[0][1] = 0
heap = [(0, 0, 1)]
while heap:
    large, free, now = heapq.heappop(heap)
    if now == N:
        print(large)
        break
    for nxt, cost in graph[now]:
        if free < K:
            if largest[free + 1][nxt] > large:
                largest[free + 1][nxt] = large
                heapq.heappush(heap, (large, free + 1, nxt))
        real = max(large, cost)
        if largest[free][nxt] > real:
            largest[free][nxt] = real
            heapq.heappush(heap, (real, free, nxt))
else:
    print(-1)
