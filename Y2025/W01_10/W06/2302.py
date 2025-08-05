import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ans = 1

dp = [0] * 42
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, 42):
    dp[i] = dp[i - 2] + dp[i - 1]

i = 1
for _ in range(M):
    to = int(sys.stdin.readline())
    ans *= dp[to - i]
    i = to + 1
ans *= dp[N + 1 - i]

print(ans)
