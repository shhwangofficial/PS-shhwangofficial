import sys

N = int(sys.stdin.readline())
mod = 9901
a, b = 1, 1
for i in range(N - 1):
    temp = a
    a = (a + (2 * b)) % mod
    b = (temp + b) % mod

print((a + (2 * b)) % mod)
