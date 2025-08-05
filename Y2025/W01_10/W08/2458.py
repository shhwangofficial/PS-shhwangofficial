N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

up = [0] * (N + 1)
down = [0] * (N + 1)


def dfs(node, direction):
    if direction:
        if not down[node]:
            for d in range(1, N + 1):
                if graph[node][d]:
                    down[node] |= dfs(d, direction)
        return down[node] | 1 << (node - 1)
    else:
        if not up[node]:
            for u in range(1, N + 1):
                if graph[u][node]:
                    up[node] |= dfs(u, direction)
        return up[node] | 1 << (node - 1)


for node in range(1, N + 1):
    dfs(node, 0)
    dfs(node, 1)

ans = 0
for node in range(1, N + 1):
    if up[node] | down[node] | 1 << (node - 1) == (1 << N) - 1:
        ans += 1
print(ans)
