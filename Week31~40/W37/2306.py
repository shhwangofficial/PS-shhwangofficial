import sys

DNA = list(sys.stdin.readline().strip())
N = len(DNA)

dp = [[0] * N for _ in range(N)]

for d in range(1, N):
    for l in range(N - d):
        r = l + d
        for k in range(l, r + 1):
            dp[l][r] = max(dp[l][r], dp[l][k - 1] + dp[k][r])
            if (DNA[l] == "a" and DNA[r] == "t") or (DNA[l] == "g" and DNA[r] == "c"):
                dp[l][r] = max(dp[l][r], dp[l + 1][r - 1] + 2)

print(dp[0][N - 1])
