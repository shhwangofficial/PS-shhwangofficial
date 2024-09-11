import sys

N, M, K = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for i in range(N + 1)]
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a < b:
        graph[a][b] = max(graph[a][b], c)

dp = graph[1][:]
lst = []
for i in range(N, 1, -1):
    if dp[i] > 0:
        lst.append(i)

turn = 1
while turn < M - 1:
    temp = set([])
    for i in lst:
        for j in range(N, i, -1):
            if graph[i][j] > 0 and dp[i] + graph[i][j] > dp[j]:
                dp[j] = dp[i] + graph[i][j]
                temp.add(j)
    if not temp:
        break
    lst = sorted(list(temp), reverse=True)
    turn += 1

print(dp[N])
