import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        if board[i][j] == "M":
            Mx, My = i, j
            break

pipe_visited = [[0] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if board[i][j] != ".":
            pipe_visited[i][j] = 1

dic = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, -1], [0, 1]],
    "+": [[-1, 0], [0, -1], [0, 1], [1, 0]],
    "1": [[0, 1], [1, 0]],
    "2": [[-1, 0], [0, 1]],
    "3": [[-1, 0], [0, -1]],
    "4": [[0, -1], [1, 0]],
}

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([])
visited[Mx][My] = 1
h_flag = 0

for i in range(4):
    nx, ny = Mx + dx[i], My + dy[i]
    if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != ".":
        visited[nx][ny] = 1
        queue.append([nx, ny])
        break

while queue:
    x, y = queue.popleft()
    n = dic[board[x][y]]
    for dx, dy in n:
        if board[x + dx][y + dy] == ".":
            hx, hy = x + dx, y + dy
            h_flag = 1
            break
        if visited[x + dx][y + dy] == 0:
            visited[x + dx][y + dy] = 1
            queue.append([x + dx, y + dy])

    if h_flag:
        break

ans = []
for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
    nx, ny = hx + dx, hy + dy
    if 0 <= nx < row and 0 <= ny < col:
        if dx == -1 and dy == 0:
            if board[nx][ny] in {"|", "+", "1", "4"}:
                ans.append([dx, dy])
        elif dx == 0 and dy == -1:
            if board[nx][ny] in {"-", "+", "1", "2"}:
                ans.append([dx, dy])
        elif dx == 0 and dy == 1:
            if board[nx][ny] in {"-", "+", "3", "4"}:
                ans.append([dx, dy])
        elif dx == 1 and dy == 0:
            if board[nx][ny] in {"|", "+", "2", "3"}:
                ans.append([dx, dy])

for key in dic:
    if dic[key] == ans:
        h_block = key
        break

print(hx + 1, hy + 1, h_block)
