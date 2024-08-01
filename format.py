import sys
N = int(sys.stdin.readline())

# 1 10  -> a = 1, b = 10
import sys
a, b = map(int,sys.stdin.readline().split())

import sys
string = sys.stdin.readline().rstrip()

# str str -> ["str", "str"]
list1 = sys.stdin.readline().split()

sys.setrecursionlimit(10**7)

# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, sys.stdin.readline().split()))

# 110110 -> [1, 1, 0, 1, 1, 0]
num_list = list(map(int, sys.stdin.readline().rstrip()))

import itertools
nCr = list(itertools.combinations(num_list, 3))
# -> [(), (), ...]

# 2차원 행렬 만들기
import sys
N = int(sys.stdin.readline())
mat = []
for _ in range(N):
    r = sys.stdin.readline()
    tmp = []
    for j in range(N):
        tmp.append(int(r[j])) # input에 따라 조절 필요
    mat.append(tmp)

import copy
b = copy.deepcopy(a)