import sys
import heapq

N = int(sys.stdin.readline())

graph = [[0] * N for _ in range(N)]

stars = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        dist = (((stars[i][0] - stars[j][0]) ** 2) + ((stars[i][1] - stars[j][1]) ** 2)) ** (1 / 2)

        graph[i][j], graph[j][i] = dist, dist


connected = [0] * N
connected[0] = 1
heap = [(0, 0)]
total = 1
sum_dist = 0
while heap:
    dist, now = heapq.heappop(heap)
    if not connected[now]:
        total += 1
        sum_dist += dist
        connected[now] = 1
    if total == N:
        print(sum_dist)
        break
    for i in range(N):
        if not connected[i]:
            heapq.heappush(heap, (graph[now][i], i))
