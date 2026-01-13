import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import math

N, M = map(int, input().split())
needs = [int(input()) for _ in range(N)]
s = max(needs)
e = 100000 * 10000

while s <= e:
    mid = (s + e) // 2
    cnt, val = 1, mid
    for need in needs:
        if val < need:
            val = 0
            times = math.ceil(need / mid)
            cnt += times
            val += mid * times
        val -= need
    if cnt > M:
        s = mid + 1
    else:
        ans = mid
        e = mid - 1

print(ans)
