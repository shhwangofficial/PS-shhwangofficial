import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

board = [list(map(int, input().split())) for _ in range(9)]
empty = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            empty.append(r * 9 + c)


def dfs(i, board):
    r, c = empty[i] // 9, empty[i] % 9
    for put in range(1, 10):
        board[r][c] = put
        if validation(r, c, board):
            if i == len(empty) - 1:
                for row in board:
                    print(*row)
                exit()
            dfs(i + 1, board)
    board[r][c] = 0


def validation(r, c, board):
    checker = [0] * 10
    for col in range(9):
        if board[r][col] == 0:
            continue
        if checker[board[r][col]] == 1:
            return False
        checker[board[r][col]] += 1
    checker = [0] * 10
    for row in range(9):
        if board[row][c] == 0:
            continue
        if checker[board[row][c]] == 1:
            return False
        checker[board[row][c]] += 1
    checker = [0] * 10
    pr, pc = (r // 3) * 3, (c // 3) * 3
    for dr in range(3):
        for dc in range(3):
            if board[pr + dr][pc + dc] == 0:
                continue
            if checker[board[pr + dr][pc + dc]] == 1:
                return False
            checker[board[pr + dr][pc + dc]] += 1
    return True


dfs(0, board)
