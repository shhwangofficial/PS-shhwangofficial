import sys

N = int(sys.stdin.readline())

if N % 2:
    print(0)
else:
    N = N // 2
    dp = [0, 3]
    sum_ = 0
    for i in range(N - 1):
        dp.append(dp[-1] * 3 + 2 * sum_ + 2)
        sum_ += dp[-2]
    print(dp[N])
