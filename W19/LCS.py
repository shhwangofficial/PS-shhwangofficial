import sys

str1 = "s" + str(sys.stdin.readline().strip())
str2 = "s" + str(sys.stdin.readline().strip())
dp = []
for i in range(len(str2)):
    dp.append([0] * len(str1))

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str2[i] == str1[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

if dp[-1][-1] == 0:
    print(0)
else:
    i = -1
    j = -1
    result = []
    while dp[i][j] != 0:
        if dp[i - 1][j - 1] == dp[i - 1][j] and dp[i - 1][j] == dp[i][j - 1]:
            if dp[i - 1][j - 1] < dp[i][j]:
                result.append(i)
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] <= dp[i][j - 1]:
                j -= 1
            else:
                i -= 1
    print(len(result))
    for i in range(len(result) - 1, -1, -1):
        print(str2[result[i]], end="")
