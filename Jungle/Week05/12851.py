import sys
from collections import deque
col, row = map(int,sys.stdin.readline().split())

tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
ripen = deque([])
for i in range(row):
    for j in range(col):
        if tomatos[i][j] == 1:
            ripen.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


while ripen:
    now = ripen.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0<=nx<row and 0<=ny<col:
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[now[0]][now[1]] + 1
                ripen.append([nx, ny])
                
flag = 1
max_day = 0
for i in range(row):
    for j in range(col):
        if tomatos[i][j] == 0:
            flag = 0
            break
        max_day = max(max_day, tomatos[i][j])
if flag == 0:
    print(-1)
else:
    print(max_day-1)
              