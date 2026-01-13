import sys
from collections import defaultdict

L, U = map(int, sys.stdin.readline().split())

dic = defaultdict(int)  # 0


def solve(num):
    if num < 0:
        return 0
    if 0 <= num <= 9:
        return (num) * (num + 1) // 2

    if not dic[num]:
        top, rest = int(str(num)[0]), int(str(num)[1:])
        dic[num] = top * (rest + 1) + solve(rest) + solve(num - rest - 1)

    return dic[num]


print(solve(U) - solve(L - 1))
