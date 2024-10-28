import sys, heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

inf = 10**9
fox = [inf] * (N + 1)
fox[1] = 0
heap = [(0, 1)]
while heap:
    cost, now = heapq.heappop(heap)
    if fox[now] < cost:
        continue
    for next, d in graph[now]:
        if fox[next] > cost + d:
            fox[next] = cost + d
            heapq.heappush(heap, (fox[next], next))

wolf = [[inf] * (N + 1) for _ in range(2)]
wolf[0][1] = 0
heap = [(0, 1, 0)]
while heap:
    cost, now, t = heapq.heappop(heap)
    if wolf[t][now] < cost:
        continue
    if t == 0:
        mult = 0.5
    else:
        mult = 2
    for next, d in graph[now]:
        alt = 1 - t
        if wolf[alt][next] > cost + (d * mult):
            wolf[alt][next] = cost + (d * mult)
            heapq.heappush(heap, (wolf[alt][next], next, alt))

ans = 0
for i in range(N + 1):
    if fox[i] < wolf[0][i] and fox[i] < wolf[1][i]:
        ans += 1

print(ans)
