import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()


def build_tree(s, e, i):
    if s == e:
        tree[i] = lst[s]
        return tree[i]
    mid = (s + e) // 2
    left = build_tree(s, mid, 2 * i)
    right = build_tree(mid + 1, e, 2 * i + 1)
    tree[i] = left + right
    return tree[i]


def find_tree(s, e, fr, to, i):
    if s == e:
        return tree[i]
    if s == fr and e == to:
        return tree[i] + (lazy[i] * (e - s + 1))
    mid = (s + e) // 2
    if lazy[i] != 0:
        propagation(s, mid, 2 * i, lazy[i])
        propagation(mid + 1, e, 2 * i + 1, lazy[i])
        tree[i] += lazy[i] * (e - s + 1)
        lazy[i] = 0

    if mid < fr:
        return find_tree(mid + 1, e, fr, to, 2 * i + 1)
    elif to <= mid:
        return find_tree(s, mid, fr, to, 2 * i)
    else:
        return find_tree(s, mid, fr, mid, 2 * i) + find_tree(mid + 1, e, mid + 1, to, 2 * i + 1)


def propagation(s, e, i, val):
    if s == e:
        tree[i] += val
    else:
        lazy[i] += val


def fix_tree(s, e, fr, to, i, val):
    if s == e:
        tree[i] += val
        return
    if s == fr and e == to:
        lazy[i] += val
        return

    mid = (s + e) // 2
    if lazy[i] != 0:
        propagation(s, mid, 2 * i, lazy[i])
        propagation(mid + 1, e, 2 * i + 1, lazy[i])
        tree[i] += lazy[i] * (e - s + 1)
        lazy[i] = 0

    if mid + 1 <= fr:
        fix_tree(mid + 1, e, fr, to, 2 * i + 1, val)
    elif to <= mid:
        fix_tree(s, mid, fr, to, 2 * i, val)
    else:
        fix_tree(s, mid, fr, mid, 2 * i, val)
        fix_tree(mid + 1, e, mid + 1, to, 2 * i + 1, val)

    tree[i] += val * (to - fr + 1)

    return


N, M, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
tree = [0] * (4 * N)
lazy = [0] * (4 * N)
build_tree(0, N - 1, 1)
for _ in range(M + K):
    comm = list(map(int, input().split()))
    if comm[0] == 1:
        fix_tree(0, N - 1, comm[1] - 1, comm[2] - 1, 1, comm[3])
    elif comm[0] == 2:
        print(find_tree(0, N - 1, comm[1] - 1, comm[2] - 1, 1))
