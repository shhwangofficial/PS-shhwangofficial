import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
rev_graph = [[] for i in range(N+1)]
directed_by = [0 for i in range(N+1)]
time_construct = [0]
for i in range(1, N+1):
    num = list(map(int, sys.stdin.readline().split()))
    time_construct.append(num[0])
    for j in range(1, len(num)-1):
        directed_by[i] += 1
        graph[num[j]].append(i)
        rev_graph[i].append(num[j])

queue = deque([])
for i in range(1, len(directed_by)):
    if directed_by[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    max_time = 0
    for i in range(len(rev_graph[now])):
        max_time = max(max_time, time_construct[rev_graph[now][i]])
    time_construct[now] += max_time
    for i in graph[now]:
        directed_by[i] -= 1
        if directed_by[i] == 0:
            queue.append(i)
        
for i in range(1, len(time_construct)):
    print(time_construct[i])