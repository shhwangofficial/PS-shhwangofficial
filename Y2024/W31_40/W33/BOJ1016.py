import sys

a, b = map(int, sys.stdin.readline().split())
ans = [1] * (b - a + 1)
last_num = int(b ** (1 / 2))
prime = [True] * (last_num + 1)
for i in range(2, last_num + 1):
    if prime[i] == True:
        for j in range(2 * i, last_num + 1, i):
            prime[j] = False

for i in range(2, last_num + 1):
    if prime[i] == True:
        squared = i**2
        if a % squared == 0:
            start = 0
        else:
            start = (a // squared + 1) * squared - a
        for j in range(start, len(ans), squared):
            ans[j] = 0

print(sum(ans))
