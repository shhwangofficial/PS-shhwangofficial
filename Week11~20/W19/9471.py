import sys

N = int(sys.stdin.readline())
dp = [1, 1, 1, 2, 2, 3]
for i in range(100):
    dp.append(dp[-1] + dp[-5])
for i in range(N):
    print(dp[int(sys.stdin.readline()) - 1])
