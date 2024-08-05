import sys

N = int(sys.stdin.readline())
MOD = 1000000007
num = sorted(list(map(int, sys.stdin.readline().split())))
res = 0
for i in range(N):
    res += num[i] * (pow(2, i, MOD) - 1) - num[i] * (pow(2, N - i - 1, MOD) - 1)
print(res % MOD)
