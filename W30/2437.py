import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

sum_ = num[0]
if sum_ != 1:
    print(1)
else:
    for i in range(1, len(num)):
        if sum_ + 1 < num[i]:
            break
        else:
            sum_ += num[i]

    print(sum_ + 1)
