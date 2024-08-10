import sys

T = int(sys.stdin.readline())
for _ in range(T):
    len_num = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * len_num for i in range(len_num)]

    s = [0] * (len_num + 1)
    for i in range(len_num):
        s[i] = s[i - 1] + num[i]

    for k in range(1, len_num):
        for i in range(len_num - k):
            j = i + k
            dp[i][j] = min(dp[i][mid] + dp[mid + 1][j] for mid in range(i, j))
            dp[i][j] += s[j] - s[i - 1]

    print(dp[0][len_num - 1])
