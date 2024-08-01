import sys, heapq
N, M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
inf = int(10**9)
min_distance = [inf for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start_node = 1
min_distance[start_node] = 0
heap = [[min_distance[start_node], start_node]]
end_node = N

while heap:
    now = heapq.heappop(heap)
    if now[1] == end_node:
        result = now[0]
        break
    for line in graph[now[1]]:
        if min_distance[line[0]] > now[0] + line[1]:
            min_distance[line[0]] = now[0] + line[1]
            heapq.heappush(heap, [min_distance[line[0]], line[0]])

print(result)