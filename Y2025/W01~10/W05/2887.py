import sys
import heapq

N = int(sys.stdin.readline())
nodes = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]


graph = [[] for i in range(N)]

for d in (0, 1, 2):
    nodes.sort(key=lambda x: x[d])
    for i in range(N - 1):
        graph[nodes[i][3]].append((nodes[i + 1][3], abs(nodes[i][d] - nodes[i + 1][d])))
        graph[nodes[i + 1][3]].append((nodes[i][3], abs(nodes[i][d] - nodes[i + 1][d])))

connected = [0] * (N)
conn = 0
min_edge = [float("inf")] * (N)
min_edge[0] = 0
heap = [[0, 0]]
ans = 0
while heap:
    dist, now = heapq.heappop(heap)
    if not connected[now]:
        ans += dist
        connected[now] = 1
        conn += 1
        if conn == N:
            break
        for next, cost in graph[now]:
            if not connected[next] and cost < min_edge[next]:
                min_edge[next] = cost
                heapq.heappush(heap, [cost, next])
print(ans)
