import sys

N = 1000001
candies = [0] * N
seg_tree = [0] * (4 * N)


def find_rank(rank, start, end, idx):
    if start == end:
        return start
    mid = (start + end) // 2
    if seg_tree[idx * 2] >= rank:
        return find_rank(rank, start, mid, idx * 2)
    else:
        return find_rank(rank - seg_tree[idx * 2], mid + 1, end, idx * 2 + 1)


def fix_tree(at, val, start, end, idx):
    if start == at and end == at:
        seg_tree[idx] += val
        return seg_tree[idx]
    mid = (start + end) // 2
    if at <= mid:
        seg_tree[idx] = fix_tree(at, val, start, mid, idx * 2) + seg_tree[2 * idx + 1]
    else:
        seg_tree[idx] = fix_tree(at, val, mid + 1, end, idx * 2 + 1) + seg_tree[2 * idx]
    return seg_tree[idx]


n = int(sys.stdin.readline())
for _ in range(n):
    comm = list(map(int, sys.stdin.readline().split()))
    if comm[0] == 1:
        rank = comm[1]
        at = find_rank(rank, 0, N - 1, 1)
        print(at)
        fix_tree(at, -1, 0, N - 1, 1)
    else:
        at = comm[1]
        val = comm[2]
        fix_tree(at, val, 0, N - 1, 1)
