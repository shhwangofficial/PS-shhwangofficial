import sys

verdict_penalty = 0
lst = []
for i in range(11):
    a, b = map(int, sys.stdin.readline().split())
    lst.append(a)
    verdict_penalty += b * 20

lst.sort()
for i in range(1, 11):
    lst[i] += lst[i - 1]


print(sum(lst) + verdict_penalty)
