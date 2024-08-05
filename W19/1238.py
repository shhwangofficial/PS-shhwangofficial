import heapq
import sys

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
inf = 10**8


for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])


def dijkstra(start, end):
    min_dist = [inf for i in range(N + 1)]
    min_dist[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        now = heapq.heappop(heap)
        if now[1] == end:
            return now[0]
        else:
            for i in range(len(graph[now[1]])):
                if min_dist[graph[now[1]][i][0]] > now[0] + graph[now[1]][i][1]:
                    min_dist[graph[now[1]][i][0]] = now[0] + graph[now[1]][i][1]
                    heapq.heappush(
                        heap, [min_dist[graph[now[1]][i][0]], graph[now[1]][i][0]]
                    )


max_ = 0
for i in range(1, N + 1):
    if i == X:
        continue
    max_ = max(max_, (dijkstra(i, X) + dijkstra(X, i)))

print(max_)
