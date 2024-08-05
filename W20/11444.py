import sys

N = int(sys.stdin.readline())

memo_dict = {}
memo_dict[1] = 1
memo_dict[2] = 1
MOD = 1000000007


def Fibo(num):
    if num in memo_dict:
        return memo_dict[num]

    if num % 2 == 0:
        half = num // 2
        memo_dict[num] = Fibo(half) * (Fibo(half - 1) + Fibo(half + 1)) % MOD
    else:
        half = (num + 1) // 2
        memo_dict[num] = (Fibo(half) ** 2 + Fibo(half - 1) ** 2) % MOD

    return memo_dict[num]


print(Fibo(N))
