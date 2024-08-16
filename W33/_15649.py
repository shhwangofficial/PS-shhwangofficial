import sys
# from itertools import permutations

# a, b = map(int, sys.stdin.readline().split())
# for i in permutations(range(1, a+1), b):
#     print(*i)

a, b = map(int, sys.stdin.readline().split())


def permutation(lst, res):
    for i in range(len(lst)):
        res_temp = res+[lst[i]]
        lst_temp = lst[:i] + lst[i+1:]
        if len(res_temp) == b:
            print(*res_temp)
        else:
            permutation(lst_temp, res_temp)
        

permutation(list(range(1, a+1)), [])
