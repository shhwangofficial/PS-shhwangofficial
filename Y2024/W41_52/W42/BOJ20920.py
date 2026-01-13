import sys
from collections import defaultdict

dic = defaultdict(int)
N, M = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    if len(string) >= M:
        if not dic[string]:
            lst.append(string)
        dic[string] += 1


lst.sort(key=lambda x: (-dic[x], -len(x), x))
for s in lst:
    print(s)
