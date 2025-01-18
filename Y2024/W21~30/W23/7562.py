import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
    board_size = int(sys.stdin.readline())
    board = [[0] * board_size for i in range(board_size)]
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    queue = deque([[sx, sy, 0]])
    board[sx][sy] = 1
    movement_x = [1, 2, 2, 1, -1, -2, -2, -1]
    movement_y = [2, 1, -1, -2, -2, -1, 1, 2]

    while queue:
        now = queue.popleft()
        now_x, now_y, now_t = now[0], now[1], now[2]
        if now_x == ex and now_y == ey:
            print(now_t)
            break
        for k in range(8):
            newx = now_x + movement_x[k]
            newy = now_y + movement_y[k]
            if 0 <= newx < board_size and 0 <= newy < board_size:
                if board[newx][newy] == 0:
                    board[newx][newy] = 1
                    queue.append([newx, newy, now_t + 1])
