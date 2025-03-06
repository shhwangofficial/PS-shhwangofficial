import sys
sys.stdin = open("python_input.txt", "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 1 10  -> a = 1, b = 10
a, b = map(int, input().split())

# str str -> ["str", "str"]
list1 = input().split()

sys.setrecursionlimit(10**7)

# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, input().split()))

# 110110 -> [1, 1, 0, 1, 1, 0]
num_list = list(map(int, input()))


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
