import sys
N = int(sys.stdin.readline())
time = []
price = []
for i in range(N):
   a, b = map(int,sys.stdin.readline().split())
   time.append(a)
   price.append(b)

dp = [0 for i in range(N+1)]

max_val = 0
for i in range(N-1, -1, -1):
    if time[i] + i <= N:
        val = dp[time[i] + i] + price[i]
        max_val = max(val, max_val)
    
    dp[i] = max_val

print(dp[0])