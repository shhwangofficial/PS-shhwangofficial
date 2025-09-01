import heapq

N, M = map(int, input().split())
vision = list(map(int, input().split()))
vision[-1] = 0

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    if vision[a] == 0 and vision[b] == 0:
        graph[a].append((b, t))
        graph[b].append((a, t))

distance = [float("inf")] * N
distance[0] = 0
heap = [(0, 0)]  # (현재까지 거리, 현재 노드)

while heap:
    d, now = heapq.heappop(heap)

    if distance[now] < d:
        continue

    for nxt, cost in graph[now]:
        new_cost = d + cost
        if distance[nxt] > new_cost:
            distance[nxt] = new_cost
            heapq.heappush(heap, (new_cost, nxt))

print(distance[N - 1] if distance[N - 1] != float("inf") else -1)
