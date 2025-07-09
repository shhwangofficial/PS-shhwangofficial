import sys

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst == [0]:
        break
    lst.append(0)

    stack = []
    max_area = 0
    for idx in range(1, len(lst)):
        base = idx
        while stack and stack[-1][1] >= lst[idx]:
            base, height = stack.pop()
            max_area = max((idx - base) * (height), max_area)
        stack.append([base, lst[idx]])

    print(max_area)
