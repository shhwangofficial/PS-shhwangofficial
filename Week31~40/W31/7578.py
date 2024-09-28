import sys
from math import ceil, log2

N = int(sys.stdin.readline())
dic = dict()
A = list(map(int, sys.stdin.readline().split()))
for i, num in enumerate(A):
    dic[num] = i

H = ceil(log2(N))
len_tree = 2 ** (H + 1)
seg_tree = [0] * len_tree


def tree(now, start, end, idx):
    if now == start:
        return seg_tree[idx]
    mid = (start + end) // 2
    if now <= mid:
        return tree(now, start, mid, 2 * idx) + seg_tree[idx * 2 + 1]
    else:
        return tree(now, mid + 1, end, 2 * idx + 1)


def fix_tree(now, start, end, idx):
    seg_tree[idx] += 1
    if start == end:
        return
    mid = (start + end) // 2
    if now <= mid:
        fix_tree(now, start, mid, 2 * idx)
    else:
        fix_tree(now, mid + 1, end, 2 * idx + 1)


B = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in B:
    cnt += tree(dic[num] + 1, 0, N - 1, 1)
    fix_tree(dic[num], 0, N - 1, 1)

print(cnt)
