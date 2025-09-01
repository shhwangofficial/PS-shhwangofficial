import sys

N, M = map(int, sys.stdin.readline().split())

attr = list(map(int, sys.stdin.readline().split()))

s = 0
e = 2000000000 * 30 + 1
temp = e
while s <= e:
    mid = (s + e) // 2
    sum_ = 0
    for a in attr:
        sum_ += mid // a + 1

    if sum_ >= N:
        temp = mid
        e = mid - 1
    else:
        s = mid + 1

for a in attr:
    N -= (temp - 1) // a + 1

for i in range(len(attr)):
    if temp % attr[i] == 0:
        N -= 1
        if N == 0:
            print(i + 1)
            break
