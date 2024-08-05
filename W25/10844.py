import sys

N = int(sys.stdin.readline())
dp = [[0 for j in range(10)] for i in range(N)]

for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, N):
    for j in range(10):
        if j <= 8:
            dp[i][j] += dp[i - 1][j + 1]
        if j >= 1:
            dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] %= 1000000000

res = 0
for j in range(10):
    res += dp[N - 1][j]
    res %= 1000000000
print(res)
