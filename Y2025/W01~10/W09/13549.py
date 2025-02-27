N, M = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(N)]
for r in range(N):
    for c in range(M):
        if board[r][c] == "B":
            Br, Bc = r, c
            board[r][c] = "."
        elif board[r][c] == "R":
            Rr, Rc = r, c
            board[r][c] = "."
        elif board[r][c] == "O":
            Gr, Gc = r, c

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def roll_red(Rr, Rc, Br, Bc, d):
    while True:
        nRr, nRc = Rr + dr[d], Rc + dc[d]
        if board[nRr][nRc] == "#":
            return Rr, Rc, Br, Bc
        elif nRr == Br and nRc == Bc:
            nBr, nBc = roll_blue(Rr, Rc, Br, Bc, d)
            if nBr == -1:
                return -2, -2, -2, -2
            elif nBr != Br or nBc != Bc:  # 파란 공이 굴렀어
                Br, Bc = nBr, nBc
                continue
            else:
                return Rr, Rc, Br, Bc
        elif board[nRr][nRc] == "O":
            return -1, -1, Br, Bc
        Rr, Rc = nRr, nRc


def roll_blue(Rr, Rc, Br, Bc, d):
    while True:
        nBr, nBc = Br + dr[d], Bc + dc[d]
        if board[nBr][nBc] == "#":
            return Br, Bc
        elif nBr == Rr and nBc == Rc:
            return Br, Bc
        elif board[nBr][nBc] == "O":
            return -1, -1
        Br, Bc = nBr, nBc


def backtrack(turn, Rr, Rc, Br, Bc, before):
    if turn >= 10:
        return False
    ret = False
    for d in set(range(4)) - set([before]):
        nRr, nRc, nBr, nBc = roll_red(Rr, Rc, Br, Bc, d)
        if nRr == -2:
            continue
        nBr, nBc = roll_blue(nRr, nRc, nBr, nBc, d)
        if nRr == -1:
            if nBr == -1:
                continue
            else:
                return True
        else:
            ret = ret or backtrack(turn + 1, nRr, nRc, nBr, nBc, d)
    return ret


print(1 if backtrack(0, Rr, Rc, Br, Bc, -1) else 0)
