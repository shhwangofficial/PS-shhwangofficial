import math
import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

height = 2 ** (math.ceil(math.log2(N)) + 1)
tree = [0] * height


def make_tree(start=0, end=N - 1, idx=1):
    if start == end:
        tree[idx] = start
        return start

    mid = (start + end) // 2
    left = make_tree(start, mid, 2 * idx)
    left_val = num[left]
    right = make_tree(mid + 1, end, 2 * idx + 1)
    right_val = num[right]
    if left_val <= right_val:
        tree[idx] = left
        return left
    else:
        tree[idx] = right
        return right


def update_tree(idx, start=0, end=N - 1, idx_tree=1):
    if start == end:
        return
    mid = (start + end) // 2
    if start <= idx <= mid:
        update_tree(idx, start, mid, 2 * idx_tree)
    elif mid < idx <= end:
        update_tree(idx, mid + 1, end, 2 * idx_tree + 1)
    tree[idx_tree] = (
        tree[2 * idx_tree]
        if num[tree[2 * idx_tree]] <= num[tree[2 * idx_tree + 1]]
        else tree[2 * idx_tree + 1]
    )


def get_tree(from_idx, to_idx, start=0, end=N - 1, tree_idx=1):
    if start == end or (from_idx == start and to_idx == end):
        return tree[tree_idx]

    mid = (start + end) // 2
    if mid < from_idx:
        return get_tree(from_idx, to_idx, mid + 1, end, 2 * tree_idx + 1)
    elif to_idx <= mid:
        return get_tree(from_idx, to_idx, start, mid, 2 * tree_idx)
    else:
        left = get_tree(from_idx, mid, start, mid, 2 * tree_idx)
        right = get_tree(mid + 1, to_idx, mid + 1, end, 2 * tree_idx + 1)
        return left if num[left] <= num[right] else right


make_tree()

for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        num[b - 1] = c
        update_tree(b - 1)
    else:
        print(get_tree(b - 1, c - 1) + 1)
