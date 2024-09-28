import sys

M, N, K = map(int, sys.stdin.readline().split())
board = [[0] * M for _ in range(N)]

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(a, c):
        for j in range(b, d):
            board[i][j] = 1

cnt = 0
ans = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            cnt += 1
            area = 0
            board[i][j] = 1
            stack = [(i, j)]
            while stack:
                now_x, now_y = stack.pop()
                area += 1
                for k in range(4):
                    new_x, new_y = now_x + dx[k], now_y + dy[k]
                    if 0 <= new_x < N and 0 <= new_y < M and board[new_x][new_y] == 0:
                        board[new_x][new_y] = 1
                        stack.append((new_x, new_y))
            ans.append(area)

print(cnt)
print(*sorted(ans))
