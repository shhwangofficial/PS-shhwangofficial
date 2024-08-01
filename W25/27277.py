import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()


res = sum(num[(len(num))//2:]) - sum(num[:(len(num)+1)//2-1])
print(res)