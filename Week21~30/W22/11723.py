import sys

N = int(sys.stdin.readline())
S = 0
for _ in range(N):
    num = list(map(str, sys.stdin.readline().split()))
    if len(num) > 1:
        num[1] = int(num[1]) - 1
    if num[0] == "add":
        S = S | (1 << num[1])
    elif num[0] == "remove":
        S = S & ~(1 << num[1])
    elif num[0] == "check":
        print(1 if S & (1 << num[1]) > 0 else 0)
    elif num[0] == "toggle":
        S = S ^ (1 << num[1])
    elif num[0] == "all":
        S = (1 << 20) - 1
    elif num[0] == "empty":
        S = 0
