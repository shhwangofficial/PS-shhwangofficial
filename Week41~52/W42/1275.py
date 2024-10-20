import sys

N, Q = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
tree = [0] * (4 * N)


def fix_tree(s, e, i, idx, val):
    if s == e:
        tree[i] = val
        return
    mid = (s + e) // 2
    if idx <= mid:
        fix_tree(s, mid, 2 * i, idx, val)
    else:
        fix_tree(mid + 1, e, 2 * i + 1, idx, val)
    tree[i] = tree[2 * i] + tree[2 * i + 1]


def get_sum(s, e, i, fr, to):
    if s == fr and e == to:
        return tree[i]
    mid = (s + e) // 2
    if fr > mid:
        return get_sum(mid + 1, e, 2 * i + 1, fr, to)
    elif to <= mid:
        return get_sum(s, mid, 2 * i, fr, to)
    else:
        return get_sum(s, mid, 2 * i, fr, mid) + get_sum(mid + 1, e, 2 * i + 1, mid + 1, to)


for i in range(N):
    fix_tree(0, N - 1, 1, i, nums[i])

for _ in range(Q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    x -= 1
    y -= 1
    a -= 1
    print(get_sum(0, N - 1, 1, x, y))
    fix_tree(0, N - 1, 1, a, b)
