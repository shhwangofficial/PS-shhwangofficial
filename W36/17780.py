import sys

N, K = map(int, sys.stdin.readline().split())

board_color = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board_piece = [[[-1]] * N for _ in range(N)]
dxdy = [
    [],
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
]

pieces = []
for i in range(K):
    row, col, direction = map(int, sys.stdin.readline().split())
    pieces.append([i, row - 1, col - 1, direction])
    board_piece[row - 1][col - 1] = [i]


stage = 0
while stage < 1000:
    stage += 1
    for piece in pieces:
        i, r, c, d = piece
        if board_piece[r][c][0] != i:
            continue
        dx, dy = dxdy[d][0], dxdy[d][1]
        nr, nc = r + dx, c + dy
        if not (0 <= nr < N and 0 <= nc < N) or board_color[nr][nc] == 2:
            nd = (d % 2) + 1 + ((d // 3) * 2)
            dx, dy = dxdy[nd][0], dxdy[nd][1]
            nr, nc = r + dx, c + dy
            pieces[i][3] = nd
            if not (0 <= nr < N and 0 <= nc < N) or board_color[nr][nc] == 2:
                nr, nc = r, c
            else:
                if board_color[nr][nc] == 1:
                    board_piece[r][c].reverse()
                if board_piece[nr][nc] == [-1]:
                    board_piece[nr][nc] = board_piece[r][c][:]
                else:
                    board_piece[nr][nc] += board_piece[r][c][:]
                board_piece[r][c] = [-1]

        else:
            if board_color[nr][nc] == 1:
                board_piece[r][c].reverse()
            if board_piece[nr][nc] == [-1]:
                board_piece[nr][nc] = board_piece[r][c][:]
            else:
                board_piece[nr][nc] += board_piece[r][c][:]
            board_piece[r][c] = [-1]

        if len(board_piece[nr][nc]) >= 4:
            print(stage)
            exit()
        else:
            for piece in board_piece[nr][nc]:
                pieces[piece][1], pieces[piece][2] = nr, nc

else:
    print(-1)
