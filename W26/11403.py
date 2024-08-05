import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N)]

for i in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if num[j] == 1:
            graph[i].append(j)

for i in range(N):
    visited = [0] * (N)
    queue = deque([i])
    while queue:
        now = queue.popleft()
        for j in graph[now]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
    print(*visited)
