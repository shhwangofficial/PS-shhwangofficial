import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
INF = 10**8
graph = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a][b] = c

path = [[-1] * N for _ in range(1 << N)]
dp = [[0] * N for _ in range(1 << N)]


def dfs(now, visited):
    if visited == (1 << N) - 1:
        return graph[now][0]

    if dp[visited][now]:
        return dp[visited][now]

    ret, ret_nxt = INF, -1
    for nxt in range(1, N):
        if graph[now][nxt] and not visited & (1 << nxt):
            tmp = dfs(nxt, visited | (1 << nxt))
            if ret > max(tmp, graph[now][nxt]):
                ret = max(tmp, graph[now][nxt])
                ret_nxt = nxt
    dp[visited][now] = ret
    path[visited][now] = ret_nxt
    return ret


dfs(0, 1)

if dp[1][0] == INF:
    print(-1)
else:
    print(dp[1][0])
    print(1, end=" ")
    now = 0
    vis = 1 << now
    set_ = set([now])
    while True:
        val = path[vis][now]
        if val == -1:
            break
        else:
            vis |= 1 << val
            print(val + 1, end=" ")
            now = val
