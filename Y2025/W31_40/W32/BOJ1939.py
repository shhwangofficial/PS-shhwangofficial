import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A, B = A - 1, B - 1
    graph[A].append([B, C])
    graph[B].append([A, C])
s, e = map(int, input().split())
s, e = s - 1, e - 1
visited = [0] * N
heap = [(-float("inf"), s)]
ans = float("inf")
while heap:
    dist, now = heapq.heappop(heap)
    if visited[now]:
        continue
    visited[now] = 1
    dist = -dist
    ans = min(ans, dist)
    if now == e:
        print(ans)
        exit()
    for nxt, cost in graph[now]:
        if not visited[nxt]:
            heapq.heappush(heap, (-(cost), nxt))
