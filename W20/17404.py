import copy
import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(list(map(int, sys.stdin.readline().split())))


def solve(lst):

    for i in range(1, len(lst)):
        for j in range(3):
            set_ = list({0, 1, 2} - {j})
            lst[i][j] += min(lst[i - 1][set_[0]], lst[i - 1][set_[1]])
    return min(lst[-1])


lst = []
INF = 10**8
for i in range(3):
    num_inf = copy.deepcopy(num)
    for j in range(3):
        if j != i:
            num_inf[0][j] = INF
    num_inf[-1][i] = INF
    lst.append(solve(num_inf))
print(min(lst))
