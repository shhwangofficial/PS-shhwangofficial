import sys

n, m, r = map(int, sys.stdin.readline().split())

INF = int(1e9)

items = [0] + list(map(int, sys.stdin.readline().split()))

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
for a in range(1, n + 1):
    temp = 0
    for b in range(1, n + 1):
        if graph[a][b] <= m:
            temp += items[b]
    ans = max(temp, ans)

print(ans)
