import sys

N, M, K = map(int, sys.stdin.readline().split())

dp = [[0] * (M + 2) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1 + 1):
        if i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i - 1][j:])

if sum(dp[-1][1:]) < K:
    print(-1)
    exit()

temp = []
r = N
c = 1
while K > 0:
    if r == 0:
        break
    if K <= dp[r][c]:
        temp.append(c)
        r -= 1
    else:
        K -= dp[r][c]
        c += 1

ans = [""] * (2 * M + 1)
for i in range(len(ans)):
    if i % 2:
        ans[i] = "z"
for num in temp:
    ans[2 * (num - 1)] += "a"

for letters in ans:
    if letters != "":
        print(letters, end="")
