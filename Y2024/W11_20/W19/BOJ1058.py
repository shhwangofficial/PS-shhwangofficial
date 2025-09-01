import sys

N = int(sys.stdin.readline())
INF = 10**8
graph = [[INF] * (N) for i in range(N)]
for i in range(N):
    num = list(map(str, sys.stdin.readline().rstrip()))
    for j in range(len(num)):
        if num[j] == "Y":
            graph[i][j] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_ = 0
for i in range(len(graph)):
    temp = 0
    for j in range(len(graph[i])):
        if 1 <= graph[i][j] <= 2:
            temp += 1
    max_ = max(max_, temp)
print(max_)
