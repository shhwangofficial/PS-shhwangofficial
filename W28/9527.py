import math
import sys

a, b = map(int, sys.stdin.readline().split())

num = [1]
i = 1
sum_ = 1
c = 0
while i <= 56:
    c = sum_ + (2**i)
    num.append(c)
    i += 1
    sum_ += c


def from0toN(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    idx = int(N.bit_length() - 1)
    return sum(num[:idx]) + (N - (2**idx) + 1) + from0toN(N - (2**idx))


print(from0toN(b) - from0toN(a - 1))
