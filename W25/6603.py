import sys
from itertools import combinations
while True:
    num = list(map(int, sys.stdin.readline().split()))
    if num ==[0]:
        exit()

    num = num[1:]
    for i in combinations(num,6):
        print(*i)
    print()