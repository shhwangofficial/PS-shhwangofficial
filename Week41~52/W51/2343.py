import sys

N, M = map(int, sys.stdin.readline().split())

lectures = list(map(int, sys.stdin.readline().split()))

s, e = max(lectures), sum(lectures)
flag = 0
while s <= e:
    mid = (s + e) // 2
    blueray = 1
    sum_blueray = 0
    for i in range(N):
        if sum_blueray + lectures[i] > mid:
            blueray += 1
            sum_blueray = 0

        sum_blueray += lectures[i]

        if blueray > M:
            s = mid + 1
            break
    else:
        ans = mid
        e = mid - 1

print(ans)
