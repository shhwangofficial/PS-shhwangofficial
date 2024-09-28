import sys

T = int(sys.stdin.readline())
sys.setrecursionlimit(10**7)


def dfs(now):
    visited[now] = 1
    cycle.append(now)
    next = graph[now]
    if visited[next] == 1:
        if next in cycle:
            global result
            result += cycle[cycle.index(next) :]
        return
    else:
        dfs(next)


for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [0]
    graph += list(map(int, sys.stdin.readline().split()))
    visited = [0] * (N + 1)
    result = []
    for i in range(1, N + 1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    print(N - len(result))
