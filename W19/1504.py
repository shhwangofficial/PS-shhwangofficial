import heapq
import sys

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
inf = 10**9
min_distance = [inf for _ in range(N + 1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(start, end):
    min_distance = [inf for _ in range(N + 1)]
    min_distance[start] = 0
    heap = [[min_distance[start], start]]
    result = inf
    while heap:
        now = heapq.heappop(heap)
        if now[1] == end:
            result = now[0]
            break
        for line in graph[now[1]]:
            if min_distance[line[0]] > line[1] + now[0]:
                min_distance[line[0]] = line[1] + now[0]
                heapq.heappush(heap, [min_distance[line[0]], line[0]])
    return result


start, end = map(int, sys.stdin.readline().split())

flag1, flag2 = 0, 0
min1, min2 = inf, inf
if dijkstra(1, start) == inf or dijkstra(start, end) == inf or dijkstra(end, N) == inf:
    flag1 = 1
else:
    min1 = dijkstra(1, start) + dijkstra(start, end) + dijkstra(end, N)

if dijkstra(1, end) == inf or dijkstra(end, start) == inf or dijkstra(start, N) == inf:
    flag2 = 1
else:
    min2 = dijkstra(1, end) + dijkstra(end, start) + dijkstra(start, N)

if flag1 * flag2 == 1:
    print(-1)
else:
    print(min(min1, min2))
