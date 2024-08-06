import heapq
import sys
from collections import deque

Inf = 10**7
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    s, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N)]
    rev_graph = [[] for _ in range(N)]
    for _ in range(M):
        road = list(map(int, sys.stdin.readline().split()))
        graph[road[0]].append([road[1], road[2]])

    min_ = Inf

    min_dist = [Inf] * N
    min_dist[s] = 0
    heap = [[0, s]]
    while heap:
        dist, now = heapq.heappop(heap)
        if now == e:
            if dist <= min_:
                min_ = dist
                continue
            else:
                break
        for next, cost in graph[now]:
            if min_dist[next] == dist + cost:
                rev_graph[next].append(now)
            elif min_dist[next] > dist + cost:
                min_dist[next] = dist + cost
                rev_graph[next] = [now]
                heapq.heappush(heap, [min_dist[next], next])

    queue = deque([e])
    visited = [0] * N
    visited[e] = 1
    while queue:
        now = queue.popleft()
        for rev in rev_graph[now]:
            for i in graph[rev]:
                if i[0] == now:
                    i[1] = Inf
                    break
            if visited[rev] == 0:
                queue.append(rev)
                visited[rev] = 1

    min_dist = [Inf] * N
    min_dist[s] = 0
    heap = [[0, s]]
    while heap:
        dist, now = heapq.heappop(heap)
        if now == e:
            break
        for next, cost in graph[now]:
            if min_dist[next] > dist + cost:
                min_dist[next] = dist + cost
                heapq.heappush(heap, [min_dist[next], next])

    print(-1 if min_dist[e] == Inf else min_dist[e])
