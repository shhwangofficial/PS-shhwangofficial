import sys
N = int(sys.stdin.readline())
mat = []
for i in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))

from itertools import combinations

set_full = set(range(N))

min_ = 999999
for combination in combinations(range(N), N//2):
    set_A = set(combination)
    set_B = set_full - set_A
    score = 0
    for couple in combinations(combination, 2):
        score += mat[couple[0]][couple[1]]
        score += mat[couple[1]][couple[0]]
    for couple in combinations(set_B, 2):
        score -= mat[couple[0]][couple[1]]
        score -= mat[couple[1]][couple[0]]
    if score == 0:
        print(0)
        exit()
    elif min_ > abs(score):
        min_ = abs(score)

print(min_)