import sys
from math import sqrt
N = int(sys.stdin.readline())

dp = [0] * (N+1)
squares = []
for i in range(1, int(sqrt(N))+1):
    j = i**2
    dp[j] = 1
    squares.append(j)

for i in range(2, N+1):
    min_ = 999999
    for square in squares:
        if i - square < 0:
            break
        elif i - square == 0:
            min_ = 0
            break
        else:
            if dp[i - square] < min_:
                min_ = dp[i - square]
    dp[i] = min_ + 1

print(dp[-1])