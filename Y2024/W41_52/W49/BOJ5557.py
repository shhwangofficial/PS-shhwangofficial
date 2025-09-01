import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 21 for _ in range(N - 1)]

dp[0][num[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] > 0:
            if j + num[i] <= 20:
                dp[i][j + num[i]] += dp[i - 1][j]
            if j - num[i] >= 0:
                dp[i][j - num[i]] += dp[i - 1][j]

print(dp[-1][num[-1]])
