import sys

N, M = map(int, sys.stdin.readline().split())


def union(v1, v2):
    r1 = find_root(v1)
    r2 = find_root(v2)

    if r1 < r2:
        root[r2] = r1
    else:
        root[r1] = r2


def find_root(v1):
    while v1 != root[v1]:
        v1 = root[v1]

    return v1


root = [i for i in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if find_root(a) == find_root(b):
        print(i + 1)
        break
    union(a, b)

else:
    print(0)
