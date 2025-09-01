import sys

sys.setrecursionlimit(10**5)
row, col = map(int, sys.stdin.readline().split())

board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(row)]

dp = [[0] * col for _ in range(row)]
ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
set_ = set([])


def backtrack(dp, r, c, set_):
    set_.add((r, c))
    jump = int(board[r][c])
    temp = 0

    for i in range(4):
        nr, nc = r + (jump * dx[i]), c + (jump * dy[i])
        if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != "H":
            if (nr, nc) in set_:
                print(-1)
                exit()
            if dp[nr][nc]:
                temp = max(temp, dp[nr][nc] + 1)
            else:
                temp = max(temp, backtrack(dp, nr, nc, set_) + 1)
        else:
            temp = max(temp, 1)

    dp[r][c] = temp
    set_.remove((r, c))
    return temp


print(backtrack(dp, 0, 0, set_))
