N = int(input())
dp = [0, 1, 3]
if N <= 2:
    print(dp[N])
else:
    i = 2
    while True:
        dp.append((dp[-1] + dp[-2] * 2) % 10007)
        i += 1
        if i == N:
            print(dp[i])
            break
