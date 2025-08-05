import heapq
import sys

no_cities = int(sys.stdin.readline())
no_lines = int(sys.stdin.readline())
graph = [[] for _ in range(no_cities + 1)]
path = [0 for _ in range(no_cities + 1)]
for _ in range(no_lines):
    at, to, c = map(int, sys.stdin.readline().split())
    graph[at].append([c, to])

start, end = map(int, sys.stdin.readline().split())
inf = 10**8
min_dist = [inf for i in range(no_cities + 1)]
min_dist[start] = 0
heap = [[0, start]]
while heap:
    cost, now = heapq.heappop(heap)
    if now == end:
        min_dist[end] = cost
        break
    for line in graph[now]:
        if min_dist[line[1]] > cost + line[0]:
            min_dist[line[1]] = cost + line[0]
            heapq.heappush(heap, [min_dist[line[1]], line[1]])
            path[line[1]] = now

spot = end
res = []
while path[spot] != start:
    res.append(path[spot])
    spot = path[spot]
res.reverse()

print(min_dist[end])
print(2 + len(res))
print(start, *res, end)
