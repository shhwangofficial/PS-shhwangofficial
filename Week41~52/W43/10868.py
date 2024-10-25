import sys

N, M = map(int, sys.stdin.readline().split())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

tree = [0] * (4 * N)


def make_tree(s, e, idx):
    if s == e:
        tree[idx] = nums[s]
        return

    mid = (s + e) // 2
    make_tree(s, mid, 2 * idx)
    make_tree(mid + 1, e, 2 * idx + 1)

    tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])


def get_min(s, e, idx, fr, to):
    if s == fr and e == to:
        return tree[idx]
    mid = (s + e) // 2
    if fr > mid:
        return get_min(mid + 1, e, 2 * idx + 1, fr, to)
    elif to <= mid:
        return get_min(s, mid, 2 * idx, fr, to)
    else:
        return min(get_min(s, mid, 2 * idx, fr, mid), get_min(mid + 1, e, 2 * idx + 1, mid + 1, to))


make_tree(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(get_min(0, N - 1, 1, a - 1, b - 1))
