import sys

board = []
N = 10
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
min_cost = -1


def some_left(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                return (i, j)
    return (-1, -1)


def backtrack(board, lst, cost):
    if -1 in lst:
        return
    row, col = some_left(board)
    if row >= 0 and col >= 0:
        for k in range(1, 6):
            flag = 0
            for i in range(0, k):
                for j in range(0, k):
                    if (0 <= row + i < N and 0 <= col + j < N) and board[row + i][col + j] == 1:
                        pass
                    else:
                        flag = 1
                        break
                if flag == 1:
                    break
            else:
                for i in range(0, k):
                    for j in range(0, k):
                        board[row + i][col + j] = 0
                lst[k] -= 1
                backtrack(board, lst, cost + 1)
                lst[k] += 1
                for i in range(0, k):
                    for j in range(0, k):
                        board[row + i][col + j] = 1

    else:
        global min_cost
        if min_cost == -1:
            min_cost = cost
        else:
            min_cost = min(min_cost, cost)


backtrack(board, [5, 5, 5, 5, 5, 5], 0)
print(min_cost)
