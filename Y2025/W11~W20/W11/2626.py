import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
riders = list(map(int, input().split()))
max_ = int(input())

dp = [[0] * (N) for _ in range(4)]
cum_sum = [0] * (N + 1)
cum_sum[0] = riders[0]
for i in range(1, N):
    cum_sum[i] = cum_sum[i - 1] + riders[i]

for r in range(1, 4):
    for c in range(max_ * r - 1, N):
        dp[r][c] = max(dp[r - 1][c - max_] + (cum_sum[c] - cum_sum[c - max_]), dp[r][c - 1])

print(dp[3][N - 1])
