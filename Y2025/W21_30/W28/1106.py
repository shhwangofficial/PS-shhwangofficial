import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

C, N = map(int, input().split())
dp = [0] * (C + 1000)
for _ in range(N):
    cost, customer = map(int, input().split())
    if dp[customer] == 0:
        dp[customer] = cost
    else:
        dp[customer] = min(cost, dp[customer])
    for i in range(1, len(dp)):
        if dp[i] and i + customer < len(dp):
            if dp[i + customer] == 0:
                dp[customer + i] = cost + dp[i]
            else:
                dp[customer + i] = min(cost + dp[i], dp[customer + i])

for i in range(len(dp)):
    if dp[i] == 0:
        dp[i] = float("inf")

print(min(dp[C : len(dp)]))
