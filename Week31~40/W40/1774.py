import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[float("inf")] * (N) for i in range(N)]
spots = []
for _ in range(N):
    spots.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(i + 1, N):
        length = ((spots[i][0] - spots[j][0]) ** 2 + (spots[i][1] - spots[j][1]) ** 2) ** 0.5
        graph[i][j] = length
        graph[j][i] = length

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a, b = a - 1, b - 1
    graph[a][b] = 0
    graph[b][a] = 0

sum_ = 0
connected_dots = 0
heap = [[0, 0]]
connected = [0 for i in range(N)]
while heap:
    length, now = heapq.heappop(heap)
    if connected[now] == 0:
        connected[now] = 1
        sum_ += length
        connected_dots += 1
        if connected_dots == N:
            break
        for i in range(N):
            if connected[i] == 0:
                heapq.heappush(heap, [graph[now][i], i])

sum_ = round(sum_, 2)
print(f"{sum_:.2f}")
