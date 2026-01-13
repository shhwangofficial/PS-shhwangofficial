import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
tree = [0] * (4 * N)


def make_tree(s, e, idx):
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]

    mid = (s + e) // 2
    tree[idx] = min(make_tree(s, mid, 2 * idx), make_tree(mid + 1, e, 2 * idx + 1))
    return tree[idx]


def fix_tree(s, e, i, j, idx):
    if s == e:
        tree[idx] = j
        return tree[idx]

    mid = (s + e) // 2
    if i <= mid:
        fix_tree(s, mid, i, j, 2 * idx)
    else:
        fix_tree(mid + 1, e, i, j, 2 * idx + 1)
    tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])
    return tree[idx]


def get_tree(s, e, i, j, idx):
    if s == i and e == j:
        return tree[idx]

    mid = (s + e) // 2
    if mid < i:
        return get_tree(mid + 1, e, i, j, 2 * idx + 1)
    elif mid >= j:
        return get_tree(s, mid, i, j, 2 * idx)
    else:
        return min(get_tree(s, mid, i, mid, 2 * idx), get_tree(mid + 1, e, mid + 1, j, 2 * idx + 1))


make_tree(0, N - 1, 1)

M = int(sys.stdin.readline())
for _ in range(M):
    comm, i, j = map(int, sys.stdin.readline().split())
    if comm == 1:
        i -= 1
        fix_tree(0, N - 1, i, j, 1)
    else:
        i, j = i - 1, j - 1
        print(get_tree(0, N - 1, i, j, 1))
