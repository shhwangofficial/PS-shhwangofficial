import sys

N, L, R = map(int, sys.stdin.readline().split())

dp = [[[0] * (N + 1) for _ in range(N + 1)] for i in range(N + 1)]
dp[1][1][1] = 1
mod = 1000000007

for n in range(1, N):
    for l in range(1, n + 1):
        for r in range(1, n + 1):
            if dp[n][l][r]:
                dp[n + 1][l + 1][r] += dp[n][l][r] % mod
                dp[n + 1][l][r + 1] += dp[n][l][r] % mod
                dp[n + 1][l][r] += (dp[n][l][r] * (n - 1)) % mod

print(dp[N][L][R] % mod)
