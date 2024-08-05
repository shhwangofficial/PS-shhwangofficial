import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
graph = [[] for i in range(a + 1)]
directed = [0] * (a + 1)
directed[0] = 1
for _ in range(b):
    num = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(num) - 1):
        graph[num[i]].append(num[i + 1])
        directed[num[i + 1]] += 1
res = []
queue = deque([])
for i in range(1, len(directed)):
    if directed[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    res.append(now)
    for next in graph[now]:
        directed[next] -= 1
        if directed[next] == 0:
            queue.append(next)
if len(res) == a:
    for i in res:
        print(i)
else:
    print(0)
