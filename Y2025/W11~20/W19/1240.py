import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for _ in range(M):
    fr, to = map(int, input().split())
    stack = [(fr, 0)]
    visited = set([fr])
    while stack:
        now, cost = stack.pop()
        if now == to:
            print(cost)
            break
        for nxt in range(1, N + 1):
            if graph[now][nxt] and nxt not in visited:
                visited.add(nxt)
                stack.append((nxt, cost + graph[now][nxt]))
