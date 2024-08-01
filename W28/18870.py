import sys
N = int(sys.stdin.readline())

# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, sys.stdin.readline().split()))

set_ = list(set(num))
set_.sort()
dict_ = {}
for i, val in enumerate(set_):
    dict_[val] = i
for n in num:
    print(dict_[n], end = ' ')
