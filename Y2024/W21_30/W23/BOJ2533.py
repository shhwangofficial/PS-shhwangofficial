import sys

sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
visited = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 1] for i in range(N + 1)]


def dfs(start):
    visited[start] = 1
    for next in graph[start]:
        if visited[next] == 0:
            if len(graph[next]) > 1:
                dfs(next)
            dp[start][0] += dp[next][1]
            dp[start][1] += min(dp[next])


dfs(1)
print(min(dp[1]))
