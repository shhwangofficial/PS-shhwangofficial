import sys

N, M = map(int, sys.stdin.readline().split())
memories = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

dp = [-1] * (sum(costs) + 1)
dp[0] = 0

for i in range(N):
    for j in range(len(dp) - 1, -1, -1):
        if j - costs[i] < 0:
            break
        if dp[j - costs[i]] >= 0:
            if dp[j] == -1:
                dp[j] = memories[i] + dp[j - costs[i]]
            else:
                dp[j] = max(dp[j], memories[i] + dp[j - costs[i]])

for i in range(len(dp)):
    if dp[i] >= M:
        print(i)
        break
