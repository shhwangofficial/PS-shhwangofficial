import sys

N = int(sys.stdin.readline())
coord = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
inf = 10**8
dp = [[-1] * ((1 << N) + 1) for _ in range(N)]


def dist(A, B):
    return ((coord[A][0] - coord[B][0]) ** 2 + (coord[A][1] - coord[B][1]) ** 2) ** (
        1 / 2
    )


def DFS(now, visited):
    if visited == (1 << N) - 1:
        return dist(now, 0)
    if dp[now][visited] != -1:
        return dp[now][visited]

    min_ = inf
    for next in range(N):
        if visited & (1 << next) == 0:
            min_ = min(min_, DFS(next, visited | (1 << next)) + dist(now, next))
    dp[now][visited] = min_
    return min_


print(DFS(0, 1))
