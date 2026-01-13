import sys, heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

heap = [(0, 1)]
distance = [float("inf")] * (N + 1)
distance[1] = 0
connected = [0] * (N + 1)
lines = [0] * (N + 1)
while heap:
    cost, now = heapq.heappop(heap)
    if not connected[now]:
        connected[now] = 1
        for to in range(1, N + 1):
            if cost + graph[now][to] < distance[to]:
                distance[to] = cost + graph[now][to]
                heapq.heappush(heap, (cost + graph[now][to], to))
                lines[to] = now

print(N - 1)
for i in range(2, len(lines)):
    print(i, lines[i])
