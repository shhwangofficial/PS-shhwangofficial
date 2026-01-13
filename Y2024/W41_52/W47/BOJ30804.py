import sys
from itertools import combinations

N = int(sys.stdin.readline())

stick = list(map(int, sys.stdin.readline().split()))


ans = 0
for c in combinations(range(1, 10), 2):
    temp = 0
    temp_max = 0
    for f in stick:
        if f in c:
            temp += 1
            temp_max = max(temp_max, temp)
        else:
            temp = 0

    ans = max(ans, temp_max)

print(ans)
