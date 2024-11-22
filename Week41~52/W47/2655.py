import sys

N = int(sys.stdin.readline())

bricks = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]
bricks.sort()

dp = [[0] * N for _ in range(N)]
seq = [[[] for i in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = bricks[i][1]
    seq[i][i] = [bricks[i][3]]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(i, j):
            if bricks[k][2] <= bricks[j][2]:
                if dp[i][k] + bricks[j][1] > dp[i][j]:
                    dp[i][j] = dp[i][k] + bricks[j][1]
                    seq[i][j] = seq[i][k][:] + [bricks[j][3]]

height = 0
for i in range(N):
    for j in range(N):
        if height < dp[i][j]:
            height = dp[i][j]
            ans = seq[i][j]

print(len(ans))
for i in ans:
    print(i + 1)
