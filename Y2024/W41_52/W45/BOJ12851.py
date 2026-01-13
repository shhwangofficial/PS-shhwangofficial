import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visited = [999999] * 100001
route = 0
queue = deque([(N, 0)])
visited[N] = 0

while queue:
    now, step = queue.popleft()
    if now == K:
        if visited[K] > step:
            route = 1
            visited[K] = step
        elif visited[K] == step:
            route += 1
        continue

    for new in (now - 1, now + 1, now * 2):
        if 0 <= new <= 100000 and visited[new] >= step + 1:
            visited[new] = step + 1
            queue.append((new, step + 1))


print(visited[K])
print(route)
