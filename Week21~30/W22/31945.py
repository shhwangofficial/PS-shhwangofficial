import sys

N = int(sys.stdin.readline())
set_ = [
    [0, 1, 2, 3],
    [0, 1, 4, 5],
    [4, 5, 6, 7],
    [2, 3, 6, 7],
    [1, 3, 5, 7],
    [0, 2, 4, 6],
]
for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
    if num in set_:
        print("YES")
    else:
        print("NO")
