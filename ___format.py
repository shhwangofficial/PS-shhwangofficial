import sys

N = int(sys.stdin.readline())

# 1 10  -> a = 1, b = 10
a, b = map(int, sys.stdin.readline().split())

# rstrip = rightstrip
string = sys.stdin.readline().rstrip()

# str str -> ["str", "str"]
list1 = sys.stdin.readline().split()

sys.setrecursionlimit(10**7)

# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, sys.stdin.readline().split()))

# 110110 -> [1, 1, 0, 1, 1, 0]
num_list = list(map(int, sys.stdin.readline().rstrip()))


import itertools

nCr = list(itertools.combinations(num_list, N))
# -> [(), (), ...]


import copy

copied_list = copy.deepcopy(list1)


# 입력이 있을때까지 받기
while True:
    try:
        line = input()
    except EOFError:
        break
