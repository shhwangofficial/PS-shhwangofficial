import sys

N, K = map(int, sys.stdin.readline().split())
color = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board = [[[] for i in range(N)] for j in range(N)]
piece_dic = dict()
for i in range(1, K + 1):
    r, c, d = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    piece_dic[i] = [r, c, d]
    board[r][c].append(i)

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def check_4(r, c):
    if len(board[r][c]) >= 4:
        print(t)
        exit()


def blue(piece, r, c, d, stack):
    nd = d + 1 if d % 2 else d - 1
    piece_dic[piece][2] = nd
    move(r, c, nd, stack, 1)


def move(r, c, d, stack, depth):
    nr, nc = r + dx[d], c + dy[d]
    if 0 <= nr < N and 0 <= nc < N:
        if color[nr][nc] in (0, 1):
            if color[nr][nc] == 1:
                stack.reverse()
            board[nr][nc] += stack
            check_4(nr, nc)
            for p in stack:
                piece_dic[p][0], piece_dic[p][1] = nr, nc
        else:
            if depth == 0:
                blue(piece, r, c, d, stack)
            else:
                board[r][c] += stack
    else:
        if depth == 0:
            blue(piece, r, c, d, stack)
        else:
            board[r][c] += stack


t = 1
while t <= 1000:
    for piece in range(1, K + 1):
        r, c, d = piece_dic[piece]
        for i in range(len(board[r][c])):
            if board[r][c][i] == piece:
                idx = i
                break
        stack = board[r][c][idx:]
        board[r][c] = board[r][c][:idx]
        move(r, c, d, stack, 0)
    t += 1

print(-1)
