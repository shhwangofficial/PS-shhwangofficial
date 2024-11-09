import sys

R, C, T = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for i in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

found = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == -1:
            puri_r = r
            found = 1
            break
    if found:
        break

for t in range(T):
    spread_board = [[0] * C for i in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                now = board[r][c]
                left = now
                for i in range(4):
                    nr, nc = r + dx[i], c + dy[i]
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] >= 0:
                        spread_board[nr][nc] += int(now / 5)
                        left -= int(now / 5)
                spread_board[r][c] += left

    for up_r in range(puri_r - 1, 0, -1):
        spread_board[up_r][0] = spread_board[up_r - 1][0]
    for dw_r in range(puri_r + 2, R - 1):
        spread_board[dw_r][0] = spread_board[dw_r + 1][0]
    for c in range(C - 1):
        for r in (0, R - 1):
            spread_board[r][c] = spread_board[r][c + 1]
    for up_r in range(0, puri_r):
        spread_board[up_r][C - 1] = spread_board[up_r + 1][C - 1]
    for dw_r in range(R - 1, puri_r + 1, -1):
        spread_board[dw_r][C - 1] = spread_board[dw_r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        for r in (puri_r, puri_r + 1):
            spread_board[r][c] = spread_board[r][c - 1]
    spread_board[puri_r][1] = 0
    spread_board[puri_r + 1][1] = 0
    spread_board[puri_r + 1][0] = -1
    spread_board[puri_r][0] = -1

    board = spread_board

ans = 0
for i in range(R):
    for j in range(C):
        ans += board[i][j] if board[i][j] > 0 else 0
print(ans)
