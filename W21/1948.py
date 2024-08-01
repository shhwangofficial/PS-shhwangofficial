import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

num_directed_by = [0] * (N+1)
directed_by_which = [[] for i in range(N+1)]
max_cost = [0] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    num_directed_by[b] += 1
    graph[a].append([b,c])

start, end = map(int,sys.stdin.readline().split())

queue = deque([])
for i in range(1, N+1):
    if num_directed_by[i] == 0:
        queue.append(i)
        
result = [0]
while queue:
    now = queue.popleft()
    result.append(now)
    for i in range(len(graph[now])):
        num_directed_by[graph[now][i][0]] -= 1
        if num_directed_by[graph[now][i][0]] == 0:
            queue.append(graph[now][i][0])

for i in range(N+1):
    if result[i] == start:
        start_idx = i
        continue
    if result[i] == end:
        end_idx = i

result = result[start_idx: end_idx+1]

for departure in result:
    for arrival, cost in graph[departure]:
        if max_cost[arrival] < max_cost[departure] + cost:
            directed_by_which[arrival] = [departure]
            max_cost[arrival] = max_cost[departure] + cost
        elif max_cost[arrival] == max_cost[departure] + cost:
            directed_by_which[arrival].append(departure)

queue = deque([directed_by_which[end_idx]])
visited = [0] * (N+1)
length = 0
while queue:
    now = queue.popleft()
    length += len(now)
    for city in now:
        if visited[city] == 0:
            visited[city] = 1
            queue.append(directed_by_which[city])

print(max_cost[end_idx])
print(length)
