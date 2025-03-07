import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N = int(input())

group = [i for i in range(N + 1)]
rank = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(20)]
dist = [[0] * (N + 1) for _ in range(20)]
edges = [[] for i in range(N + 1)]
visited = [0] * (N + 1)

for i in range(N - 1):
    a, b, cost = map(int, input().split())
    edges[a].append([b, cost])
    edges[b].append([a, cost])

queue = deque([(1, 1)])
visited[1] = 1
while queue:
    now, now_rank = queue.popleft()
    for nxt, cost in edges[now]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            parent[0][nxt] = now
            dist[0][nxt] = cost
            rank[nxt] = now_rank + 1
            queue.append((nxt, now_rank + 1))

for r in range(1, 20):
    for c in range(1, N + 1):
        parent[r][c] = parent[r - 1][parent[r - 1][c]]
        dist[r][c] = dist[r - 1][c] + dist[r - 1][parent[r - 1][c]]

for m in range(int(input())):
    a, b = map(int, input().split())

    if rank[a] > rank[b]:
        a, b = b, a

    ans = 0
    rank_diff = abs(rank[b] - rank[a])

    while rank_diff:
        for i in range(20):
            if rank_diff & (1 << i):
                ans += dist[i][b]
                b = parent[i][b]
                rank_diff -= 1 << i
                break

    while True:
        if a == b:
            break
        for step in range(19, -1, -1):
            if parent[step][a] != parent[step][b]:
                ans += dist[step][b] + dist[step][a]
                a, b = parent[step][a], parent[step][b]
                break
        else:
            ans += dist[0][b] + dist[0][a]
            break

    print(ans)
