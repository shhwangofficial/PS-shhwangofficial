import sys
from collections import deque

V, E = map(int, sys.stdin.readline().split())

directed_by = [0] * (V + 1)
graph = [[] for i in range(V + 1)]
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())
    directed_by[b] += 1
    graph[a].append(b)

queue = deque([])
for i in range(1, V + 1):
    if directed_by[i] == 0:
        queue.append([i, 1])

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for i in range(len(graph[now[0]])):
        directed_by[graph[now[0]][i]] -= 1
        if directed_by[graph[now[0]][i]] == 0:
            queue.append([graph[now[0]][i], now[1] + 1])

for i in range(1, V + 1):
    for j in range(0, len(result)):
        if result[j][0] == i:
            print(result[j][1], end=" ")
            break
