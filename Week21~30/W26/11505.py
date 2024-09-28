import sys
from math import ceil, log2

N, M, K = map(int, sys.stdin.readline().split())

lst = []
mod = 1000000007
for i in range(N):
    lst.append(int(sys.stdin.readline()))
H = ceil(log2(N))
len_tree = 2 ** (H + 1) - 1
tree = [0] * (len_tree + 1)


def making_tree(start, end, val):
    if start == end:
        tree[val] = lst[start] % mod
        return tree[val]
    new_end = (start + end) // 2
    tree[val] = making_tree(start, new_end, 2 * val) * making_tree(new_end + 1, end, 2 * val + 1) % mod
    return tree[val]


def update_tree(start, end, idx, val, to_val):
    if start == end:
        tree[val] = to_val % mod
        return tree[val]
    new_end = (start + end) // 2
    if idx <= new_end:
        tree[val] = update_tree(start, new_end, idx, 2 * val, to_val) * tree[2 * val + 1] % mod
    else:
        tree[val] = tree[2 * val] * update_tree(new_end + 1, end, idx, 2 * val + 1, to_val) % mod
    return tree[val]


def query(start, end, idx, from_val, to_val):
    if start == from_val and end == to_val:
        return tree[idx] % mod
    new_end = (start + end) // 2
    if new_end < from_val:
        return query(new_end + 1, end, 2 * idx + 1, from_val, to_val) % mod
    elif to_val <= new_end:
        return query(start, new_end, 2 * idx, from_val, to_val) % mod
    else:
        return (
            query(start, new_end, 2 * idx, from_val, new_end)
            * query(new_end + 1, end, 2 * idx + 1, new_end + 1, to_val)
            % mod
        )


making_tree(0, N - 1, 1)
for i in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update_tree(0, N - 1, b - 1, 1, c)
    else:
        print(query(0, N - 1, 1, b - 1, c - 1))
