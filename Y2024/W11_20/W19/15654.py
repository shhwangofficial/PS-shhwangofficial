import sys

N, M = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))
num.sort()


def backtrack(list1):
    if len(list1) == M:
        print(*list1)
        return

    for i in range(len(num)):
        if num[i] in list1:
            continue
        backtrack(list1 + [num[i]])


for i in range(N):
    backtrack([num[i]])
