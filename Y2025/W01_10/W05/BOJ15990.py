import sys

T = int(sys.stdin.readline())
MOD = 1000000009
max_ = 3
dp = [[0] * 1000001 for _ in range(4)]
dp[1][1] = 1
dp[2][2] = 1
dp[1][3], dp[2][3], dp[3][3] = 1, 1, 1
for t in range(T):
    N = int(sys.stdin.readline())
    if N <= 2:
        print(1)
        continue

    if N >= max_:
        for col in range(max_ + 1, N + 1):
            set_ = set([1, 2, 3])
            for row in set_:
                for rest in set_ - set([row]):
                    dp[row][col] = (dp[row][col] + dp[rest][col - row]) % MOD
        max_ = N

    ans = 0
    for row in range(4):
        ans = (ans + dp[row][N]) % MOD
    print(ans)
