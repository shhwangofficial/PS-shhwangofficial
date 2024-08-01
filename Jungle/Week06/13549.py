# BFS, appendleft 활용
import sys
from collections import deque
a, b = map(int,sys.stdin.readline().split())
visited = [0] *100001
visited[a] = 1
queue = deque([[0, a]])

while queue:
    # print(queue)
    now = queue.popleft()
    
    if now[1] == b:
        print(now[0])
    else:
        if 0<=now[1]*2<len(visited) and visited[now[1]*2] == 0 :
            queue.appendleft([now[0], now[1]*2])
            visited[now[1]*2] = 1
        if 0<=now[1]-1<len(visited) and visited[now[1]-1] == 0:
            queue.append([now[0]+1, now[1]-1])
            visited[now[1]-1] = 1
        if 0<=now[1]+1<len(visited) and visited[now[1]+1] == 0:
            queue.append([now[0]+1, now[1]+1])
            visited[now[1]+1] = 1