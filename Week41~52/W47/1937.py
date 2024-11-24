import sys

sys.setrecursionlimit(500 * 500)
N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(r, c):
    temp = 0
    for d in range(4):
        nr, nc = r + dx[d], c + dy[d]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] > board[r][c]:
            if dp[nr][nc]:
                temp = max(temp, dp[nr][nc])
            else:
                temp = max(temp, dfs(nr, nc))

    dp[r][c] = temp + 1
    return temp + 1


ans = 0
for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            ans = max(ans, dfs(i, j))

print(ans)
