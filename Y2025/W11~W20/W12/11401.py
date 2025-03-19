import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

MOD = 1000000007


def pac(N):
    ret = 1
    while N >= 1:
        ret = (ret * N) % MOD
        N -= 1
    return ret


def pow(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    if power not in power_dict[base]:
        power_dict[base][power] = (pow(base, power // 2) * pow(base, power // 2) * pow(base, power % 2)) % MOD
    return power_dict[base][power]


N, K = map(int, input().split())
a, b, c = pac(N), pac(K), pac(N - K)
power_dict = {b: dict(), c: dict()}
ans = (a * pow(b, MOD - 2) * pow(c, MOD - 2)) % MOD
print(ans)
