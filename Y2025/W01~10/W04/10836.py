import sys

M, N = map(int, sys.stdin.readline().split())

command = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
add_table = [[0] * M for _ in range(M)]
board = [[1] * M for _ in range(M)]


adds = [0] * (2 * M)
for stage in range(N):
    com = command[stage]
    adds[com[0]] += 1
    adds[com[0] + com[1]] += 1

for i in range(1, 2 * M - 1):
    adds[i] += adds[i - 1]

i = 0
r, c = M - 1, 0
while i < len(adds) - 1:
    add_table[r][c] += adds[i]
    if r == 0:
        c += 1
    else:
        r -= 1
    i += 1

for row in range(1, M):
    for col in range(1, M):
        add_table[row][col] = max(add_table[row - 1][col], add_table[row][col - 1], add_table[row - 1][col - 1])
for row in range(M):
    for col in range(M):
        board[row][col] += add_table[row][col]

for line in board:
    print(*line)
