import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lis = list(map(int, input().split()))
M = int(input())
dp = [-1] * (M + 1)

for i in range(len(lis) - 1, -1, -1):
    cost = lis[i]
    for j in range(cost, M + 1):
        if dp[j - cost] != -1 or j - cost == 0:
            if dp[j - cost] == -1:
                tmp = str(i)
            elif dp[j - cost] == "0":
                tmp = str(i) + "0"
            elif int(dp[j - cost] + str(i)) < int(str(i) + dp[j - cost]):
                tmp = str(i) + dp[j - cost]
            else:
                tmp = dp[j - cost] + str(i)
            if int(tmp) > int(dp[j]):
                dp[j] = str(int(tmp))

ans = 0
for i in range(M + 1):
    ans = max(ans, int(dp[i]))
print(ans)
