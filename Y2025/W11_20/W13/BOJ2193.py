import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [[0] * (N + 1) for _ in range(2)]
dp[1][1] = 1

for i in range(1, N):
    dp[0][i + 1] += dp[0][i] + dp[1][i]
    dp[1][i + 1] = dp[0][i]

print(dp[0][-1] + dp[1][-1])
