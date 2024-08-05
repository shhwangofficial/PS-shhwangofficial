import sys

N = int(sys.stdin.readline())
bit_max = (1 << 10) - 1

dp = [[[0 for _ in range(bit_max + 1)] for j in range(10)] for i in range(N)]

for j in range(1, 10):
    dp[0][j][1 << j] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(bit_max + 1):
            if j <= 8:
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]
            if j >= 1:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
            dp[i][j][k | (1 << j)] %= 1000000000

res = 0
for j in range(10):
    res += dp[N - 1][j][bit_max]
    res %= 1000000000
print(res)
