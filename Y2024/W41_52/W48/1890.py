import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1]
dy = [1, 0]


def backtrack(r, c):
    temp = 0
    for i in range(2):
        nr, nc = r + board[r][c] * dx[i], c + board[r][c] * dy[i]
        if 0 <= nr < N and 0 <= nc < N:
            if nr == N - 1 and nc == N - 1:
                temp = 1
                break
            if dp[nr][nc] >= 0:
                temp += dp[nr][nc]
            else:
                temp += backtrack(nr, nc)

    dp[r][c] = temp
    return temp


dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        if dp[i][j] > 0:
            for k in range(2):
                nr, nc = i + board[i][j] * dx[k], j + board[i][j] * dy[k]
                if 0 <= nr < N and 0 <= nc < N:
                    dp[nr][nc] += dp[i][j]

print(dp[N - 1][N - 1])
