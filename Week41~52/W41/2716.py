import sys

N = int(sys.stdin.readline())
for _ in range(N):
    string = list(map(str, sys.stdin.readline().rstrip()))
    max_ = 0
    stack = 0
    for i in range(len(string)):
        if string[i] == "[":
            stack += 1
        else:
            max_ = max(max_, stack)
            stack -= 1
    print(2**max_)
