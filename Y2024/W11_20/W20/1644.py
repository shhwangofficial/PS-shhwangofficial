import sys
from math import sqrt

N = int(sys.stdin.readline())
if N == 2:
    print(1)
else:
    num_list = [True] * (N + 1)
    num_list[0], num_list[1] = False, False
    for i in range(2, int(sqrt(N)) + 1):
        for j in range(2 * i, N + 1, i):
            num_list[j] = False

    prime = []
    for i in range(2, N + 1):
        if num_list[i] == True:
            prime.append(i)

    sum_ = 5
    pt_left = 0
    pt_right = 1
    cnt = 0
    while pt_left < len(prime):
        if sum_ > N:
            sum_ -= prime[pt_left]
            pt_left += 1
        elif sum_ < N:
            pt_right += 1
            if pt_right > len(prime) - 1:
                break
            sum_ += prime[pt_right]
        elif sum_ == N:
            cnt += 1
            sum_ -= prime[pt_left]
            pt_left += 1
            pt_right += 1
            if pt_right > len(prime) - 1:
                break
            sum_ += prime[pt_right]

    print(cnt)
