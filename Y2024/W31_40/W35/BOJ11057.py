import sys

N = int(sys.stdin.readline())
c = 10007
lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(N - 1):
    temp = [0] * 11
    temp[0] = 1
    for j in range(1, 10):
        temp[j] = (temp[j - 1] + lst[j]) % c
    lst = temp

print(sum(lst) % c)
