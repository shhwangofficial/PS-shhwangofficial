import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
i = 2
while i <= N:
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007
    i += 1
print(dp[N])
