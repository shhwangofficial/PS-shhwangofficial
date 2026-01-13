import sys
from collections import deque
from math import log2, floor

N = int(sys.stdin.readline())
graph = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

power = 17
dp = [[0] * (N + 1) for i in range(power + 1)]
rank = [0] * (N + 1)
parent = [0] * (N + 1)
visited = [0] * (N + 1)
visited[1] = 1
queue = deque([(1, 0)])

while queue:
    node, rank_now = queue.popleft()
    rank[node] = rank_now
    for child in graph[node]:
        if visited[child] == 0:
            visited[child] = 1
            parent[child] = node
            dp[0][child] = node
            queue.append((child, rank_now + 1))


for i in range(power - 1):
    for j in range(1, N + 1):
        dp[i + 1][j] = dp[i][dp[i][j]]


M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    while 1:
        if rank[a] == rank[b]:
            if a == b:
                print(a)
                break
            else:
                for i in range(power - 1, -1, -1):
                    if dp[i][a] != dp[i][b]:
                        a = dp[i][a]
                        b = dp[i][b]
                print(parent[a])
                break
        elif rank[a] < rank[b]:
            diff = rank[b] - rank[a]
            while diff:
                step = floor(log2(diff))
                b = dp[step][b]
                diff -= 2**step
        else:
            diff = rank[a] - rank[b]
            while diff:
                step = floor(log2(diff))
                a = dp[step][a]
                diff -= 2**step
