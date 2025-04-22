import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict


def check(r, c, v1, nr, nc, v2):
    if (
        v1 not in row_dict[r]
        and v1 not in col_dict[c]
        and v1 not in box_dict[(r // 3) * 3 + (c // 3)]
        and v2 not in row_dict[nr]
        and v2 not in col_dict[nc]
        and v2 not in box_dict[(nr // 3) * 3 + (nc // 3)]
    ):
        row_dict[r].add(v1)
        col_dict[c].add(v1)
        box_dict[(r // 3) * 3 + (c // 3)].add(v1)
        row_dict[nr].add(v2)
        col_dict[nc].add(v2)
        box_dict[(nr // 3) * 3 + (nc // 3)].add(v2)
        return True
    return False


def disc(r, c, v1, nr, nc, v2):
    row_dict[r].discard(v1)
    col_dict[c].discard(v1)
    box_dict[(r // 3) * 3 + (c // 3)].discard(v1)
    row_dict[nr].discard(v2)
    col_dict[nc].discard(v2)
    box_dict[(nr // 3) * 3 + (nc // 3)].discard(v2)


def backtrack(start, domino_taken):
    for pos in range(start, 81):
        r, c = pos // 9, pos % 9
        if board[r][c] == 0:
            for d in range(2):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < 9 and 0 <= nc < 9 and board[nr][nc] == 0:
                    for i in range(domino_len):
                        if not (domino_taken & 1 << (i)):
                            domino_taken |= 1 << (i)
                            v1, v2 = domino_list[i]
                            board[r][c], board[nr][nc] = v1, v2
                            if check(r, c, v1, nr, nc, v2):
                                if domino_taken == (1 << domino_len) - 1:
                                    return True
                                if backtrack(pos + 1, domino_taken):
                                    return True
                                disc(r, c, v1, nr, nc, v2)
                            board[r][c], board[nr][nc] = 0, 0

                            board[r][c], board[nr][nc] = v2, v1
                            if check(r, c, v2, nr, nc, v1):
                                if domino_taken == (1 << domino_len) - 1:
                                    return True
                                if backtrack(pos + 1, domino_taken):
                                    return True
                                disc(r, c, v2, nr, nc, v1)
                            board[r][c], board[nr][nc] = 0, 0

                            domino_taken = domino_taken & ~(1 << i)

            return False


dr = [1, 0]
dc = [0, 1]

num_puzzle = 0
while True:
    N = int(input())
    if N == 0:
        break

    num_puzzle += 1

    set_ = set()
    for i in range(1, 10):
        for j in range(i + 1, 10):
            set_.add((i, j))
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)
    box_dict = defaultdict(set)
    board = [[0] * 9 for _ in range(9)]

    for _ in range(N):
        U, LU, V, LV = input().split()
        U, V = int(U), int(V)
        UR, UC = ord(LU[0]) - 65, int(LU[1]) - 1
        VR, VC = ord(LV[0]) - 65, int(LV[1]) - 1
        board[UR][UC], board[VR][VC] = U, V
        row_dict[UR].add(U)
        col_dict[UC].add(U)
        box_dict[(UR // 3) * 3 + (UC // 3)].add(U)
        row_dict[VR].add(V)
        col_dict[VC].add(V)
        box_dict[(VR // 3) * 3 + (VC // 3)].add(V)
        if U > V:
            U, V = V, U
        set_.remove((U, V))

    domino_list = list(set_)
    domino_len = len(domino_list)
    fixed = list(input().split())
    for i in range(9):
        R, C = ord(fixed[i][0]) - 65, int(fixed[i][1]) - 1
        board[R][C] = i + 1
        row_dict[R].add(i + 1)
        col_dict[C].add(i + 1)
        box_dict[(R // 3) * 3 + (C // 3)].add(i + 1)

    backtrack(0, 0)
    print(f"Puzzle {num_puzzle}")
    for row in board:
        ret = ""
        for let in row:
            ret += str(let)
        print(ret)
