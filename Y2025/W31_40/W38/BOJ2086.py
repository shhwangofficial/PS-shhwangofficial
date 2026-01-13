import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())

fib = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
sum_fib = {0: 0, 1: 1, 2: 2, 3: 4, 4: 7}

MOD = 1000000000


def get_fib(n):
    if n in fib.keys():
        return fib[n]

    if n % 2:
        left = get_fib((n + 1) // 2) ** 2 % MOD
        right = get_fib((n - 1) // 2) ** 2 % MOD
    else:
        left = ((get_fib(n // 2)) * ((get_fib(n // 2 + 1) + get_fib(n // 2 - 1)) % MOD)) % MOD
        right = 0

    fib[n] = (left + right) % MOD
    return fib[n]


def get_sum_fib(n):
    if n in sum_fib.keys():
        return sum_fib[n]

    if n % 2:
        left = (get_fib((n + 1) // 2) * get_sum_fib((n + 1) // 2)) % MOD
        right = ((1 + get_fib((n - 1) // 2)) * get_sum_fib((n - 1) // 2)) % MOD

    else:
        left = ((get_fib((n // 2 + 1)) + 1) * get_sum_fib((n) // 2)) % MOD
        right = (get_fib(n // 2) * get_sum_fib(n // 2 - 1)) % MOD

    sum_fib[n] = (left + right) % MOD
    return sum_fib[n]


print((get_sum_fib(b) - get_sum_fib(a - 1)) % MOD)
