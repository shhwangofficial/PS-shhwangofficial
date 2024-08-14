import sys

rows, cols = map(int, sys.stdin.readline().split())

cnt = 0
visited = [[0] * cols for _ in range(rows)]
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(rows)]

for row in range(rows):
    stack = [[row, 0]]
    while stack:
        row_now, col_now = stack.pop()
        if col_now == cols - 1:
            cnt += 1
            break
        visited[row_now][col_now] = 1
        new_col = col_now + 1
        for i in (1, 0, -1):
            new_row = row_now + i
            if 0 <= new_row < rows:
                if visited[new_row][new_col] == 0 and board[new_row][new_col] == ".":
                    stack.append([new_row, new_col])
print(cnt)
