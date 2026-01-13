import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lis = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]

for i in range(n):
    if lis[i] >= 0:
        start = i
        break
else:
    print(max(lis))
    exit()

dp[0][0], dp[1][0] = lis[0], -float("inf")
for i in range(1, n):
    dp[0][i] = max(lis[i], dp[0][i - 1] + lis[i])
    dp[1][i] = max(dp[1][i - 1] + lis[i], dp[0][i - 1])

print(max(max(dp[0]), max(dp[1])))
