import sys

N = int(sys.stdin.readline()) - 1

board = []
for _ in range(N + 1):
    board.append(list(map(int, sys.stdin.readline().split())))

queue = [(0, 1, 1)]

if board[N][N] == 1:
    print(0)
    exit(0)

arrive = 0
while queue:
    r, c, d = queue.pop()
    if d == 1 or d == 3:
        if r == N and c + 1 == N:
            arrive += 1
            continue
        if c + 1 < N and board[r][c + 1] == 0:
            queue.append((r, c + 1, 1))
    if d == 2 or d == 3:
        if r + 1 == N and c == N:
            arrive += 1
            continue
        if r + 1 < N and board[r + 1][c] == 0:
            queue.append((r + 1, c, 2))

    if c + 1 <= N and r + 1 <= N and not board[r + 1][c + 1] and not board[r][c + 1] and not board[r + 1][c]:
        if r + 1 == N and c + 1 == N:
            arrive += 1
            continue
        queue.append((r + 1, c + 1, 3))

print(arrive)
