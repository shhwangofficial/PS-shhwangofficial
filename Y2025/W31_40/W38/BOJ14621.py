import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

N, M = map(int, input().split())
lst = list(map(str, input().split()))
isMan = [0] + [1 if lst[i] == "M" else 0 for i in range(N)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

connected = [False] * (N + 1)
heap = [(0, 1)]
ans = 0
while heap:
    cost, now = heapq.heappop(heap)
    if connected[now]:
        continue
    connected[now] = True
    ans += cost
    for next, cost in graph[now]:
        if not connected[next] and isMan[now] != isMan[next]:
            heapq.heappush(heap, (cost, next))

if False in connected[1:]:
    print(-1)
else:
    print(ans)
