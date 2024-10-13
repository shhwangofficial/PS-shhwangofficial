import sys

N, Q = map(int, sys.stdin.readline().split())
tree = [0] * (4 * N)


def fix_tree(s, e, idx, at, val):
    if s == e:
        tree[idx] += val
        return
    mid = (s + e) // 2
    if at <= mid:
        fix_tree(s, mid, 2 * idx, at, val)
    else:
        fix_tree(mid + 1, e, 2 * idx + 1, at, val)

    tree[idx] = tree[2 * idx] + tree[2 * idx + 1]


def get_sum(s, e, idx, fr, to):
    if s == fr and e == to:
        return tree[idx]
    mid = (s + e) // 2
    if mid < fr:
        return get_sum(mid + 1, e, 2 * idx + 1, fr, to)
    elif to <= mid:
        return get_sum(s, mid, 2 * idx, fr, to)
    else:
        return get_sum(s, mid, 2 * idx, fr, mid) + get_sum(mid + 1, e, 2 * idx + 1, mid + 1, to)


for _ in range(Q):
    cmd, par1, par2 = map(int, sys.stdin.readline().split())
    if cmd == 1:
        fix_tree(0, N - 1, 1, par1 - 1, par2)
    else:
        print(get_sum(0, N - 1, 1, par1 - 1, par2 - 1))
