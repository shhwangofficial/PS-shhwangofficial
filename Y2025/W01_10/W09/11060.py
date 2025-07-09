N = int(input())
nums = list(map(int, input().split()))
dp = [float("inf")] * N
dp[-1] = 0
for i in range(N - 2, -1, -1):
    length = nums[i]
    limit = min(N, i + length + 1)
    if dp[i + 1 : limit]:
        dp[i] = min(dp[i + 1 : limit]) + 1

print(-1 if dp[0] == float("inf") else dp[0])
