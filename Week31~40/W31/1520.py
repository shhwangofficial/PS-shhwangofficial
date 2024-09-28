import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

board = []
for _ in range(r):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

marking = [[0] * c for _ in range(r)]
queue = deque([])
for i in range(r):
    for j in range(c):
        flag = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < r and 0 <= ny < c and board[i][j] < board[nx][ny]:
                flag = 1
                marking[i][j] += 1
        if flag == 0:
            queue.append([i, j])

marking[0][0] = 10002
while queue:
    x, y = queue.popleft()
    if x == 0 and y == 0:
        continue
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c and board[x][y] > board[nx][ny]:
            marking[nx][ny] -= 1
            if marking[nx][ny] == 0:
                queue.append([nx, ny])

dp = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]
queue = deque([[0, 0]])
dp[0][0] = 1
while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c and marking[nx][ny] != 0 and board[nx][ny] < board[x][y]:
            dp[nx][ny] += dp[x][y]
            visited[nx][ny] += 1
            if visited[nx][ny] == marking[nx][ny]:
                queue.append([nx, ny])

print(dp[r - 1][c - 1])
