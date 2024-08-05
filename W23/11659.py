import sys

a, b = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(num)):
    num[i] += num[i - 1]
for i in range(b):
    s, e = map(int, sys.stdin.readline().split())
    s, e = s - 1, e - 1
    if s == 0:
        print(num[e])
    else:
        print(num[e] - num[s - 1])
