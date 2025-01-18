import sys

N, M, B = map(int, sys.stdin.readline().split())

board = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    max_ = max(row)


ans_time = 10**8
ans_height = 0
for h in range(max_ + 1):
    b = B
    temp_time = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > h:
                temp_time += 2 * (board[i][j] - h)
                b += board[i][j] - h
            else:
                temp_time += h - board[i][j]
                b -= h - board[i][j]
    if b < 0:
        continue
    else:
        if temp_time <= ans_time:
            ans_height = h
            ans_time = temp_time

print(ans_time, ans_height)
