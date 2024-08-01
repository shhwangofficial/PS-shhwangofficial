import sys
from math import ceil, sqrt
n = int(sys.stdin.readline())
N = 10**6

target = min(n, N)
prime = [True] * (target+1)

for i in range(2, ceil(sqrt(target))+1):
    if prime[i]:
        for j in range(i*i, target+1, i):
            prime[j] = False

num = n
primes = []
for i in range(2, target+1):
    if prime[i] and (num%i == 0):
        primes.append(i)
        while num % i == 0:
            num //= i

if num != 1:
    primes.append(num)

bit = 2**len(primes)
sum_ = 0
for i in range(1, bit):
    cnt = 0
    temp = 0
    temp1 = 1
    for j in range(len(primes)):
        if i & (1<<j):
            cnt += 1
            temp1 *= primes[j] 
    temp += n // temp1
    sum_ += (-1)**(cnt+1) * temp

print(n-sum_)

# n = int(input())
# ans = n

# for i in range(2, int(n**0.5)+1):
#     if n%i == 0:
#         while n%i == 0:
#             n//=i
#         ans -= (ans//i)

# if n>1:
#     ans -= (ans//n)

# print(ans)