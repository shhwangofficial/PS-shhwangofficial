import sys
a, b = map(int,sys.stdin.readline().split())
dp = [[0 for i in range(b+1)]]
for i in range(a):
    dp.append([0] + list(map(int, sys.stdin.readline().split())))

for i in range(1, a+1):
    for j in range(1, b+1):
        dp[i][j] += max(dp[i-1][j-1],dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])


