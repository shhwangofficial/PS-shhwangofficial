import sys

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
sum_ = num[0]
ans = 100001
while True:
    if sum_ < S:
        end += 1
        if end == N:
            break
        sum_ += num[end]
    else:
        ans = min(ans, end - start + 1)
        sum_ -= num[start]
        if start == end:
            end += 1
            if end == N:
                break
        else:
            start += 1

print(ans if ans != 100001 else 0)
