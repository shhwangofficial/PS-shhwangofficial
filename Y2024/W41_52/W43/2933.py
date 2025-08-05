import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]


def break_drop(h, c):
    global board, R, C
    board[h][c] = "."
    base_height = [[R] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    base = R - 1
    for col in range(C):
        if board[base][col] == "x":
            queue = deque([[base, col]])
            visited[base][col] = 1
            while queue:
                now_r, now_c = queue.popleft()
                for row in range(now_r + 1):
                    base_height[row][now_c] = min(base_height[row][now_c], now_r)
                for i in range(4):
                    n_r, n_c = now_r + dx[i], now_c + dy[i]
                    if 0 <= n_r < R and 0 <= n_c < C and visited[n_r][n_c] == 0 and board[n_r][n_c] == "x":
                        visited[n_r][n_c] = 1
                        queue.append([n_r, n_c])
    flag = 0
    drop_list = []
    for col in range(C):
        if flag == 1:
            break
        for row in range(R):
            if board[row][col] == "x" and visited[row][col] == 0:
                queue = deque([[row, col]])
                visited[row][col] = 1
                while queue:
                    now_r, now_c = queue.popleft()
                    drop_list.append([now_r, now_c])
                    for i in range(4):
                        n_r, n_c = now_r + dx[i], now_c + dy[i]
                        if 0 <= n_r < R and 0 <= n_c < C and visited[n_r][n_c] == 0 and board[n_r][n_c] == "x":
                            visited[n_r][n_c] = 1
                            queue.append([n_r, n_c])
                flag = 1
                break
    drop_height = 999
    for drop_r, drop_c in drop_list:
        drop_height = min(drop_height, base_height[drop_r][drop_c] - drop_r - 1)
        board[drop_r][drop_c] = "."

    for drop_r, drop_c in drop_list:
        board[drop_r + drop_height][drop_c] = "x"


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


N = int(sys.stdin.readline())
throws = list(map(int, sys.stdin.readline().split()))

for idx in range(len(throws)):
    height = R - throws[idx]
    if idx % 2 == 0:
        for col in range(C):
            if board[height][col] == "x":
                break_drop(height, col)
                break
    else:
        for col in range(C - 1, -1, -1):
            if board[height][col] == "x":
                break_drop(height, col)
                break

for line in board:
    for place in line:
        print(place, end="")
    print()
