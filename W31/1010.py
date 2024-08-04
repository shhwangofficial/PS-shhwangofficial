import sys
T = int(sys.stdin.readline())

def factorial(N, M):
    ans = 1
    i = N
    while i > 0:
        ans *= M
        M -= 1
        i -= 1
    while N > 0:
        ans //= N
        N -= 1
    return ans

for _ in range(T):
    N, M = map(int,sys.stdin.readline().split())
    print(factorial(N, M))