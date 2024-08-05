import sys
from math import gcd

N = int(sys.stdin.readline())
nums = []
nums_digit = []
remainder = []
for i in range(N):
    num = sys.stdin.readline().strip()
    nums.append(int(num))
    nums_digit.append(len(num))
K = int(sys.stdin.readline())

for i in range(N):
    remainder.append(nums[i] % K)
ten_power = []
for i in range(51):
    ten_power.append(10**i % K)

dp = [[0] * K for i in range(2**N)]
dp[0][0] = 1

for i in range(2**N):
    for j in range(N):
        if i & 1 << j == 0:
            for k in range(K):
                new_r = (k * (ten_power[nums_digit[j]]) + remainder[j]) % K
                dp[i | 1 << j][new_r] += dp[i][k]

if dp[-1][0] == 0:
    print("0/1")
else:
    gcd_ = gcd(dp[-1][0], sum(dp[-1]))
    print(f"{dp[-1][0]//gcd_}/{sum(dp[-1])//gcd_}")
