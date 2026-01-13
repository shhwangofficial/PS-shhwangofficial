import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t

import heapq

during = [0] * (N + 1)


def dijkstra(rem):
    dist = [float("inf")] * (N + 1)
    dist[1] = 0
    visited = [0] * (N + 1)
    heap = [(0, 1)]

    while heap:
        d, now = heapq.heappop(heap)
        if visited[now]:
            continue
        visited[now] = 1
        for nxt in range(1, N + 1):
            if graph[now][nxt] and not visited[nxt]:
                if d + graph[now][nxt] < dist[nxt]:
                    dist[nxt] = d + graph[now][nxt]
                    if rem == 0:
                        during[nxt] = now
                    heapq.heappush(heap, (dist[nxt], nxt))
    return dist[N]


ans = 0
original = dijkstra(0)
now = N
while now != 0:
    bef = during[now]
    graph[bef][now] = 0
    longer = dijkstra(1)
    if longer == float("inf"):
        print(-1)
        break
    else:
        ans = max(ans, longer - original)
    graph[bef][now] = 1
    now = bef
else:
    print(ans)
