import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))


ans = 0
day = arr[-1][0]
lst = []
while day > 0:
    while arr and arr[-1][0] >= day:
        lst.append(arr.pop())
    if lst:
        lst.sort(key=lambda x: (x[1]))
        ans += lst.pop()[1]

    day -= 1

print(ans)
