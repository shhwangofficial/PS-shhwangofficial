import sys

n, m = map(int, sys.stdin.readline().split())

group = [i for i in range(n + 1)]
rank = [0] * (n + 1)


def find(a):
    while a != group[a]:
        a = group[a]
    return a


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] < rank[b]:
            group[a] = b
            rank[b] = max(rank[a] + 1, rank[b])
        else:
            group[b] = a
            rank[a] = max(rank[b] + 1, rank[a])


for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
