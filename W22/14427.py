import sys
from math import ceil, log2

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
H = ceil(log2(N))
tree = [0] * (2 ** (H + 1))


def making_tree(start, end, idx):
    if start == end:
        tree[idx] = start
        return start

    mid = (start + end) // 2
    left_idx = making_tree(start, mid, idx * 2)
    left = num[left_idx]
    right_idx = making_tree(mid + 1, end, idx * 2 + 1)
    right = num[right_idx]
    if left <= right:
        tree[idx] = left_idx
        return left_idx
    else:
        tree[idx] = right_idx
        return right_idx


def update(start, end, tree_idx, num_idx):
    if start == end:
        return start
    if start <= num_idx <= end:
        mid = (start + end) // 2
        left_idx = update(start, mid, tree_idx * 2, num_idx)
        left = num[left_idx]
        right_idx = update(mid + 1, end, tree_idx * 2 + 1, num_idx)
        right = num[right_idx]
        if left <= right:
            tree[tree_idx] = left_idx
        else:
            tree[tree_idx] = right_idx

    return tree[tree_idx]


making_tree(0, N - 1, 1)
Q = int(sys.stdin.readline())
for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 2:
        print(tree[1] + 1)
    else:
        num[query[1] - 1] = query[2]
        update(0, N - 1, 1, query[1] - 1)
