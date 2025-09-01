import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

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
            queue.append((child, rank_now + 1))


M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    while 1:
        if rank[a] == rank[b]:
            if a == b:
                print(a)
                break
            elif parent[a] == parent[b]:
                print(parent[a])
                break
            else:
                a, b = parent[a], parent[b]
        elif rank[a] < rank[b]:
            i = rank[b] - rank[a]
            while i:
                b = parent[b]
                i -= 1
        else:
            i = rank[a] - rank[b]
            while i:
                a = parent[a]
                i -= 1
