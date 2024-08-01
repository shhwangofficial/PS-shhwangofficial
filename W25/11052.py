import sys
N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(num)):
    for j in range(1, i+1):
        num[i] = max(num[i], num[i-j]+num[j-1])

print(num[-1])
