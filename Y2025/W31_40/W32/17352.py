import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
root = [i for i in range(0, N + 1)]
rank = [0 for i in range(0, N + 1)]


def find_root(a):
    while a != root[a]:
        a = root[a]
    return a


def union(a, b):
    ra, rb = find_root(a), find_root(b)
    if rank[ra] == rank[rb]:
        rank[ra] += 1
        root[rb] = ra
    elif rank[ra] < rank[rb]:
        root[ra] = rb
    else:
        root[rb] = ra


for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

left = find_root(1)
for i in range(2, N + 1):
    if find_root(i) != left:
        print(1, i)
        exit()
