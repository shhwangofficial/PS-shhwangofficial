import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
inf = int(10**8)
min_distance = [inf for _ in range(N + 1)]
start_node = int(sys.stdin.readline())
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])


min_distance[start_node] = 0
heap = [[min_distance[start_node], start_node]]


while heap:
    now = heapq.heappop(heap)
    for line in graph[now[1]]:
        if min_distance[line[0]] > now[0] + line[1]:
            min_distance[line[0]] = now[0] + line[1]
            heapq.heappush(heap, [min_distance[line[0]], line[0]])


for i in range(1, len(min_distance)):
    if min_distance[i] == inf:
        print("INF")
    else:
        print(min_distance[i])
