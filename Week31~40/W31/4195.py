import sys
from collections import defaultdict


def find_parent(child):
    while True:
        if type(dic[child]) == int:
            return child
        else:
            child = dic[child]


T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    dic = defaultdict(lambda: 1)
    for i in range(F):
        a, b = sys.stdin.readline().split()
        p_a = find_parent(a)
        p_b = find_parent(b)
        if p_a == p_b:
            print(dic[p_a])
            continue
        if dic[p_a] >= dic[p_b]:
            dic[p_a] += dic[p_b]
            dic[p_b] = p_a
            print(dic[p_a])
        else:
            dic[p_b] += dic[p_a]
            dic[p_a] = p_b
            print(dic[p_b])
