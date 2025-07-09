import copy
import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_white = 0
max_black = 0


def backtrack_white(board, cnt, diagonal_11_5, diagonal_1_7, start_row):
    flag = 0
    for i in range(start_row, N):
        for j in range(N):
            if (i + j) % 2 == 0 and board[i][j] == 1:
                if diagonal_11_5[i - j + (N - 1)] and diagonal_1_7[(i + j)]:
                    flag = 1
                    diagonal_11_5[i - j + (N - 1)] = False
                    diagonal_1_7[(i + j)] = False
                    backtrack_white(board, cnt + 1, diagonal_11_5, diagonal_1_7, i)
                    diagonal_11_5[i - j + (N - 1)] = True
                    diagonal_1_7[(i + j)] = True
    if flag == 0:
        global max_white
        if max_white < cnt:
            max_white = cnt


def backtrack_black(board, cnt, diagonal_11_5, diagonal_1_7, start_row):
    flag = 0
    for i in range(start_row, N):
        for j in range(N):
            if (i + j) % 2 == 1 and board[i][j] == 1:
                if diagonal_11_5[i - j + (N - 1)] and diagonal_1_7[(i + j)]:
                    flag = 1
                    diagonal_11_5[i - j + (N - 1)] = False
                    diagonal_1_7[(i + j)] = False
                    backtrack_black(board, cnt + 1, diagonal_11_5, diagonal_1_7, i)
                    diagonal_11_5[i - j + (N - 1)] = True
                    diagonal_1_7[(i + j)] = True
    if flag == 0:
        global max_black
        if max_black < cnt:
            max_black = cnt


diagonal_11_5 = [True] * (N * 2)
diagonal_1_7 = [True] * (N * 2)
backtrack_white(board, 0, diagonal_11_5, diagonal_1_7, 0)
diagonal_11_5 = [True] * (N * 2)
diagonal_1_7 = [True] * (N * 2)
backtrack_black(board, 0, diagonal_11_5, diagonal_1_7, 0)
print(max_white + max_black)
