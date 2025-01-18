import sys

N = int(sys.stdin.readline())

temp = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]

board = [[0] * N for _ in range(N)]
board_row_reversed = [[1] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if temp[r][c] == "T":
            board[r][c] = 1
            board_row_reversed[r][c] = 0

ans = (N**2) + 1

for bit in range(2**N):
    board_temp = []
    for i in range(N):
        if bit & (1 << i):
            board_temp.append(board_row_reversed[i])
        else:
            board_temp.append(board[i])

    temp_head_sum = 0
    for col in range(N):
        temp_head_col = 0
        for row in range(N):
            temp_head_col += board_temp[row][col]
        temp_head_sum += min(temp_head_col, N - temp_head_col)
    ans = min(temp_head_sum, ans)

print(ans)
