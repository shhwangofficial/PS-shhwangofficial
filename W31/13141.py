import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
inf = 30000000
graph = [[inf] * (N + 1) for i in range(N + 1)]

for i in range(N + 1):
    graph[i][i] = 0

lines = set()
for i in range(M):
    line = tuple(map(int, sys.stdin.readline().split()))
    if graph[line[0]][line[1]] > line[2]:
        graph[line[0]][line[1]] = line[2]
    if graph[line[1]][line[0]] > line[2]:
        graph[line[1]][line[0]] = line[2]
    lines.add(line)
    lines.add((line[1], line[0], line[2]))

test = [[0] * (N + 1) for i in range(N + 1)]
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                test[a][b] = k


def func(a, b):
    if test[a][b] != 0:
        func(a, test[a][b])
        func(test[a][b], b)
    else:
        passed.add((a, b, graph[a][b]))
        passed.add((b, a, graph[a][b]))


res = inf
for ignite in range(1, N + 1):
    passed = set()
    i = ignite
    for j in range(1, N + 1):
        func(i, j)
    graph[i][0] = 0
    temp = max(graph[i])
    for leftover in lines - passed:
        temp = max(
            temp,
            (leftover[2] + abs(graph[i][leftover[0]] - graph[i][leftover[1]])) / 2
            + min(graph[i][leftover[0]], graph[i][leftover[1]]),
        )
    res = min(res, temp)

print("{:.1f}".format(res))
