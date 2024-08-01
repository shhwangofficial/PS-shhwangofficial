import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bacon_list = []
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    visited[i] = 1
    bacon = 0

    queue = deque([[0, i]])
    while queue:
        now = queue.popleft()
        bacon += now[0]
        for j in range(len(graph[now[1]])):
            if visited[graph[now[1]][j]] == 0:
               visited[graph[now[1]][j]] = 1
               queue.append([now[0]+1, graph[now[1]][j]]) 

    bacon_list.append(bacon)

print(bacon_list.index(min(bacon_list))+1)