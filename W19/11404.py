import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = 10**8
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()