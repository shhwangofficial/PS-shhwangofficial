import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()


dp = [[[0] * 21 for _ in range(21)] for i in range(21)]
dp[1][1][1] = 1

for n in range(1, 20):
    for l in range(1, 20):
        for r in range(1, 20):
            val = dp[n][l][r]
            dp[n + 1][l + 1][r] += val
            dp[n + 1][l][r + 1] += val
            dp[n + 1][l][r] += (n - 1) * val

T = int(input())
for t in range(T):
    n, l, r = map(int, input().split())
    print(dp[n][l][r])
