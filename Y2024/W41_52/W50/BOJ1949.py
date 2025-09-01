import sys

sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())


residents = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, residents[i]] for i in range(N + 1)]


def dfs(vil):
    visited[vil] = 1
    for next in graph[vil]:
        if not visited[next]:
            dfs(next)
            dp[vil][1] += dp[next][0]
            dp[vil][0] += max(dp[next][0], dp[next][1])


dfs(1)
print(max(dp[1][0], dp[1][1]))
