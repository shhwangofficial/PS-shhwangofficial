import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [i for i in range(N + 1)]
for i in range(3, N + 1):
    for j in range(3, i):
        dp[i] = max(dp[i], dp[i - j] * (j - 1))

print(dp[N])
