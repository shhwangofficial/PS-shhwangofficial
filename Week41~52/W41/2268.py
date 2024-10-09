import sys

N, M = map(int, sys.stdin.readline().split())
nums = [0] * (N + 1)
seg_tree = [0] * (4 * N)


def modify_tree(s, e, tree_idx, change_idx, val):
    if s == e:
        seg_tree[tree_idx] = val
        return
    mid = (s + e) // 2
    if change_idx <= mid:
        modify_tree(s, mid, 2 * tree_idx, change_idx, val)
    else:
        modify_tree(mid + 1, e, 2 * tree_idx + 1, change_idx, val)
    seg_tree[tree_idx] = seg_tree[tree_idx * 2] + seg_tree[tree_idx * 2 + 1]


def get_sum(s, e, tree_idx, fr, to):
    if s == fr and e == to:
        return seg_tree[tree_idx]

    mid = (s + e) // 2
    if mid < fr:
        return get_sum(mid + 1, e, 2 * tree_idx + 1, fr, to)
    elif to <= mid:
        return get_sum(s, mid, 2 * tree_idx, fr, to)
    else:
        return get_sum(s, mid, 2 * tree_idx, fr, mid) + get_sum(mid + 1, e, 2 * tree_idx + 1, mid + 1, to)


for _ in range(M):
    comm, A, B = map(int, sys.stdin.readline().split())
    if comm == 0:
        if A > B:
            A, B = B, A
        print(get_sum(1, N, 1, A, B))
    elif comm == 1:
        modify_tree(1, N, 1, A, B)
