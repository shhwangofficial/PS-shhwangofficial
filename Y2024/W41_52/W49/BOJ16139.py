import sys

string = sys.stdin.readline().rstrip()
length = len(string)

dp = [[0] * length for _ in range(26)]
for i in range(26):
    for j in range(length):
        char = chr(i + 97)
        if j == 0:
            if string[j] == char:
                dp[i][j] = 1
        else:
            if string[j] == char:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]


N = int(sys.stdin.readline())
for _ in range(N):
    alpha, s, e = sys.stdin.readline().split()
    a, s, e = ord(alpha) - 97, int(s), int(e)
    if s == 0:
        print(dp[a][e])
    else:
        print(dp[a][e] - dp[a][s - 1])
