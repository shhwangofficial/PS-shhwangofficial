import sys

sys.stdin = open("python_input.txt", "r")
input = sys.stdin.readline

import heapq

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [[float("inf")] * (N + 1) for _ in range(K + 1)]
distance[0][1] = 0
heap = [(0, 1, 0)]  # d, now, pojang
while heap:
    d, now, pojang = heapq.heappop(heap)
    if now == N:
        break
    if distance[pojang][now] < d:
        continue
    for nxt, cost in graph[now]:
        if d + cost < distance[pojang][nxt]:
            distance[pojang][nxt] = d + cost
            heapq.heappush(heap, (distance[pojang][nxt], nxt, pojang))
    if pojang < K:
        for nxt, cost in graph[now]:
            if distance[pojang + 1][nxt] > d:
                distance[pojang + 1][nxt] = d
                heapq.heappush(heap, (distance[pojang + 1][nxt], nxt, pojang + 1))
ans = float("inf")
for k in range(K + 1):
    ans = min(ans, distance[k][N])
print(ans)
