import sys

n, m = map(int, sys.stdin.readline().split())
inf = 10**8
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c
for a in range(1, n + 1):
    graph[a][a] = 0

table = [[0] * (n + 1) for _ in range(n + 1)]

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                table[a][b] = k


res = [[0] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            res[a][b] = "-"
        elif table[a][b] == 0:
            res[a][b] = b
        else:
            child = table[a][b]
            while 1:
                parent = table[a][child]
                if parent == 0:
                    res[a][b] = child
                    break
                else:
                    child = parent

for a in range(1, n + 1):
    print(*res[a][1:])
