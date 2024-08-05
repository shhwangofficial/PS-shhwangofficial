import sys

N = int(sys.stdin.readline())
dp = [0] * (10**6 + 1)
i = 2
while i <= N:
    now2 = 10**6
    now3 = 10**6

    if i % 2 == 0:
        now2 = dp[i // 2]
    if i % 3 == 0:
        now3 = dp[i // 3]
    now = min(dp[i - 1], now3, now2)
    dp[i] = now + 1
    i += 1
print(dp[N])
