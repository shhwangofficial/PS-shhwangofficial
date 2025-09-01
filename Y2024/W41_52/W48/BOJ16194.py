import sys

N = int(sys.stdin.readline())

dp = [9999999] * (N + 1)
dp[0] = 0
num = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(N + 1):
    for j in range(N + 1):
        if i + j <= N:
            dp[i + j] = min(dp[i + j], dp[j] + num[i])

print(dp[N])
