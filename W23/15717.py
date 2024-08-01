N = int(input())
c = 10**9 + 7
if N == 0:
    print(1)
    exit()

def custom_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        if exp != 1:
            base = (base * base) % mod
        exp //= 2
    return result

print(custom_pow(2, N-1, c))  