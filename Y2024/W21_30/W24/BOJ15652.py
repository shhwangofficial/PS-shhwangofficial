import sys

a, b = map(int, sys.stdin.readline().split())


def backtrack(list1):
    if len(list1) == b:
        print(*list1)
        return

    for i in range(list1[-1], a + 1):
        list1.append(i)
        backtrack(list1)
        list1.pop()


for i in range(1, a + 1):
    backtrack([i])
