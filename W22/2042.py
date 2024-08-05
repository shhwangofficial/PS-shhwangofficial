import sys
from math import ceil, log2

N, M, K = map(int, sys.stdin.readline().split())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))
H = ceil(log2(len(num)))
len_tree = 2 ** (H + 1) - 1
tree = [0] * (len_tree + 1)


def making_tree(start, end, now):
    if start == end:
        tree[now] = num[start]
        return tree[now]

    new_end = (start + end) // 2
    tree[now] = making_tree(start, new_end, now * 2) + making_tree(
        new_end + 1, end, now * 2 + 1
    )
    return tree[now]


def query_sum(start, end, left, right, idx):
    if start == left and end == right:
        return tree[idx]

    mid = (start + end) // 2
    if right <= mid:
        return query_sum(start, mid, left, right, idx * 2)
    elif mid + 1 <= left:
        return query_sum(mid + 1, end, left, right, idx * 2 + 1)
    else:
        return query_sum(start, mid, left, mid, idx * 2) + query_sum(
            mid + 1, end, mid + 1, right, idx * 2 + 1
        )


def update(start, end, idx, val, idx_of_tree):
    if start <= idx <= end:
        tree[idx_of_tree] += val

    if start == end:
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(start, mid, idx, val, idx_of_tree * 2)
    else:
        update(mid + 1, end, idx, val, idx_of_tree * 2 + 1)


making_tree(0, len(num) - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        index_of_num, to_val = b - 1, c
        val = to_val - num[index_of_num]
        update(0, len(num) - 1, index_of_num, val, 1)
        num[index_of_num] = to_val
    elif a == 2:
        left, right = b - 1, c - 1
        print(query_sum(0, len(num) - 1, left, right, 1))
