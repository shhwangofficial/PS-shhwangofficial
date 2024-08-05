import sys

N = int(sys.stdin.readline())
dict_ = {}
for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    if b == "enter":
        dict_[a] = 1
    else:
        del dict_[a]

temp = sorted(dict_.keys(), reverse=True)

for i in temp:
    print(i)
