N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[float("inf")] * (1 << N) for _ in range(N)]

for c in range(N):
    dp[0][1 << (c)] = board[0][c]

for dpr in range(0, N - 1):
    for dpc in range(1 << N):
        if dp[dpr][dpc] != float("inf"):
            for c in range(N):
                if not ((1 << c) & dpc):
                    dp[dpr + 1][(1 << c) | dpc] = min(dp[dpr + 1][(1 << c) | dpc], dp[dpr][dpc] + board[dpr + 1][c])


print(dp[N - 1][-1])
