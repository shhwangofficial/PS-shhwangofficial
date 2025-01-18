import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

queue = deque([[0, a]])
visited = [0] * 100001
visited[a] = 1
while queue:
    now = queue.popleft()

    if now[1] == b:
        print(now[0])
        break
    else:
        if now[1] * 2 <= 100000 and visited[now[1] * 2] == 0:
            queue.append([now[0] + 1, now[1] * 2])
            visited[now[1] * 2] = 1
        if now[1] + 1 <= 100000 and visited[now[1] + 1] == 0:
            queue.append([now[0] + 1, now[1] + 1])
            visited[now[1] + 1] = 1
        if now[1] > 0 and visited[now[1] - 1] == 0:
            queue.append([now[0] + 1, now[1] - 1])
            visited[now[1] - 1] = 1
