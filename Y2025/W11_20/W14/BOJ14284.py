import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())
s, t = s - 1, t - 1
dist = [float("inf")] * n
dist[s] = 0
heap = [(0, s)]
visited = set()
while heap:
    d, now = heapq.heappop(heap)
    if now in visited:
        continue
    visited.add(n)
    for nxt, cost in graph[now]:
        if nxt not in visited and d + cost < dist[nxt]:
            dist[nxt] = d + cost
            heapq.heappush(heap, (dist[nxt], nxt))

print(dist[t])
