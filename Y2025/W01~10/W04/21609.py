import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
score = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_largest_block(board):
    candidates = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] > 0:
                group_count = 0
                rainbow_count = 0
                visited[i][j] = 1
                rep_block = i * N + j
                rainbow_visited = [[0] * N for _ in range(N)]
                group_color = board[i][j]
                queue = deque([(i, j)])
                while queue:
                    row, col = queue.popleft()
                    group_count += 1
                    if board[row][col] == 0:
                        rainbow_count += 1
                    else:
                        rep_block = min(rep_block, row * N + col)
                    for d in range(4):
                        nr, nc = row + dx[d], col + dy[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if board[nr][nc] == 0 and rainbow_visited[nr][nc] == 0:
                                rainbow_visited[nr][nc] = 1
                                queue.append((nr, nc))
                            if board[nr][nc] == group_color and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                queue.append((nr, nc))
                if group_count > 1:
                    candidates.append((-group_count, -rainbow_count, -rep_block))

    if not candidates:
        return -1
    else:
        candidates.sort()
        # print(candidates)
        global score
        score += candidates[0][0] ** 2
        return -candidates[0][2]


def remove_block(block, board):
    row, col = block // N, block % N
    group_color = board[row][col]
    visited = [[0] * N for _ in range(N)]
    queue = deque([(row, col)])
    while queue:
        row, col = queue.popleft()
        board[row][col] = -2
        for d in range(4):
            nr, nc = row + dx[d], col + dy[d]
            if 0 <= nr < N and 0 <= nc < N:
                if (board[nr][nc] == group_color or board[nr][nc] == 0) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))


def gravity(board):
    for row in range(N - 2, -1, -1):
        for col in range(N - 1, -1, -1):
            if board[row][col] >= 0 and board[row + 1][col] == -2:
                temp_row = row + 1
                while temp_row < N:
                    if board[temp_row][col] == -2:
                        temp_row += 1
                    else:
                        break
                board[temp_row - 1][col], board[row][col] = board[row][col], -2


def rotation(board):
    board_temp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            board_temp[N - 1 - c][r] = board[r][c]
    return board_temp


while True:
    block = find_largest_block(board)
    if block == -1:
        break
    remove_block(block, board)
    gravity(board)
    board = rotation(board)
    gravity(board)

print(score)
