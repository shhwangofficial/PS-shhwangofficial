import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

max_ = 0
for S in range(1 << (N * M)):
    result = 0
    for row in range(N):
        row_sum = 0
        for col in range(M):
            if S & 1 << (row * M + col):
                if col != 0:
                    if S & 1 << (row * M + col - 1):
                        row_sum *= 10
                row_sum += board[row][col]
        result += row_sum
    for col in range(M):
        col_sum = 0
        for row in range(N):
            if not S & 1 << (row * M + col):
                if row != 0:
                    if not S & 1 << ((row - 1) * M + col):
                        col_sum *= 10
                col_sum += board[row][col]
        result += col_sum
    if result > max_:
        max_ = result

print(max_)
