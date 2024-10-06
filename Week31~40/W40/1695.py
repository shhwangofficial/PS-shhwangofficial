import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(N)]

for d in range(1, N):
    for i in range(N - d):
        j = i + d
        if num[i] != num[j]:
            dp[i][j] = min(dp[i + 1][j - 1] + 2, dp[i][j - 1] + 1, dp[i + 1][j] + 1)
        else:
            dp[i][j] = dp[i + 1][j - 1]

print(dp[0][N - 1])
