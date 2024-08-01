import sys
N, M = map(int,sys.stdin.readline().split())
mat = [[0]*(N+1)]
for _ in range(N):
    mat.append([0]+list(map(int, sys.stdin.readline().split())))

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = mat[i][j] + dp[i][j-1]
    for j in range(1, N+1):
        dp[i][j] += dp[i-1][j]

for _ in range(M):
    num = list(map(int, sys.stdin.readline().split()))
    calc = dp[num[2]][num[3]] - dp[num[0]-1][num[3]] - \
        dp[num[2]][num[1]-1] + dp[num[0]-1][num[1]-1]
    print(calc)

