import sys

MOD = 1000000007
N = int(sys.stdin.readline())


def power(base, pow):
    if pow == 1:
        return base
    if pow % 2 == 0:
        return ((power(base, pow // 2) % MOD) ** 2) % MOD
    elif pow % 2 == 1:
        return (((power(base, pow // 2) % MOD) ** 2) % MOD * base) % MOD


ans = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ans += (power(a, MOD - 2) * b) % MOD
    ans %= MOD
print(ans)
