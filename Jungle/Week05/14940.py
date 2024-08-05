import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[-1] * col for _ in range(row)]
ripen = deque([])
for i in range(row):
    for j in range(col):
        if tomatos[i][j] == 2:
            ripen.append([i, j])
            visited[i][j] = 0
        elif tomatos[i][j] == 0:
            visited[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while ripen:
    now = ripen.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0 <= nx < row and 0 <= ny < col:
            if tomatos[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[now[0]][now[1]] + 1
                ripen.append([nx, ny])


for i in range(row):
    print(*visited[i])
