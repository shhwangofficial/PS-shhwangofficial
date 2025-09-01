import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())
start = 1
end = k
while start <= end:
    mid = (start + end) // 2
    sum_ = 0
    for i in range(1, N + 1):
        sum_ += min(mid // i, N)
    if sum_ >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)
