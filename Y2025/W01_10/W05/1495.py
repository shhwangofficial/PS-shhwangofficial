import sys

N, S, M = map(int, sys.stdin.readline().split())
volumes = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (N + 1) for _ in range(M + 1)]
dp[S][0] = 1

for round in range(N):
    for vol in range(M + 1):
        if dp[vol][round]:
            if vol + volumes[round] <= M:
                dp[vol + volumes[round]][round + 1] += dp[vol][round]
            if vol - volumes[round] >= 0:
                dp[vol - volumes[round]][round + 1] += dp[vol][round]

for vol in range(M, -1, -1):
    if dp[vol][N]:
        print(vol)
        break
else:
    print(-1)
