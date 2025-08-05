import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip()))
score = 0
dp = [0, 1]
for i in range(2, N + 1):
    dp.append(dp[-1] + i * (i + 1) // 2)

i = 0
while i < N:
    if num[i] == 2:
        j = i + 1
        while j < N and num[j] == 2:
            j += 1
        cnt = j - i
        score += dp[cnt]
        i += cnt
    else:
        i += 1
print(score)
