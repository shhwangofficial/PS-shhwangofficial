import sys
N = int(sys.stdin.readline())
dp = [0] * (10**6 + 1)
dp[1] = [0, 0]
i = 2
while i <= N:
    now2 = 10**6
    now3 = 10**6
    
    if i%2 == 0:
        now2 = dp[i//2][0]
    if i%3 == 0:
        now3 = dp[i//3][0]
    if dp[i-1][0] <= now2 and dp[i-1][0] <= now3:
        dp[i] = [dp[i-1][0]+1, i-1]
    elif now2 <= dp[i-1][0] and now2 <= now3:
        dp[i] = [dp[i//2][0]+1, i//2]
    elif now3 <= dp[i-1][0] and now3 <= now2:
        dp[i] = [dp[i//3][0]+1, i//3]
    i += 1

print(dp[N][0])
print(N, end = ' ')
idx = dp[N][1]

while idx != 0:
    print(idx, end =' ')
    idx = dp[idx][1]
    
