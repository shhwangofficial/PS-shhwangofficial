import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
board = []
visited = []
connected = []
for _ in range(row):
    num_list = list(map(int, sys.stdin.readline().rstrip()))
    board.append(num_list)
    visited.append([0] * col)
    connected.append([0] * col)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited_checker = 0
for i in range(row):
    for j in range(col):
        if board[i][j] == 0 and visited[i][j] == 0:
            visited_checker += 1
            visited[i][j] = 1
            conn = 1
            queue = deque([[i, j]])
            queue2 = deque([])
            while queue:
                now = queue.popleft()
                queue2.append(now)
                for k in range(4):
                    nx = now[0] + dx[k]
                    ny = now[1] + dy[k]
                    if (
                        0 <= nx < row
                        and 0 <= ny < col
                        and board[nx][ny] == 0
                        and visited[nx][ny] == 0
                    ):
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
                        conn += 1
            conn %= 10
            while queue2:
                now = queue2.popleft()
                for k in range(4):
                    nx = now[0] + dx[k]
                    ny = now[1] + dy[k]
                    if (
                        0 <= nx < row
                        and 0 <= ny < col
                        and board[nx][ny] >= 1
                        and visited[nx][ny] < visited_checker
                    ):
                        board[nx][ny] += conn
                        visited[nx][ny] = visited_checker


for i in range(row):
    for j in range(col):
        print(board[i][j] % 10, end="")
    print()
