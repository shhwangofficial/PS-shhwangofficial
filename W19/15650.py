import sys

N, M = map(int, sys.stdin.readline().split())


def backtrack(start, list1):
    if len(list1) == M:
        print(*list1)
        return

    for i in range(start + 1, N + 1):
        backtrack(i, list1 + [i])


for i in range(1, N + 1):
    backtrack(i, [i])
