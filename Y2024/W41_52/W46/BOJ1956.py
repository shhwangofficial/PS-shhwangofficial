import sys

V, E = map(int, sys.stdin.readline().split())
inf = 10**8
graph = [[inf] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
for i in range(V + 1):
    graph[i][i] = 0


for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

ans = inf

for a in range(1, V + 1):
    for b in range(1, V + 1):
        if a == b:
            continue
        ans = min(ans, graph[a][b] + graph[b][a])


print(-1 if ans == inf else ans)
