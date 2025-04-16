import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))
tree = [0] * (4 * N)


def make_tree(s, e, tree_idx):
    if s == e:
        tree[tree_idx] = 1 if lst[s] % 2 else 0
    else:
        mid = (s + e) // 2
        tree[tree_idx] = make_tree(s, mid, 2 * tree_idx) + make_tree(mid + 1, e, 2 * tree_idx + 1)
    return tree[tree_idx]


def find_tree(s, e, tree_idx, fr, to):
    if s == fr and e == to:
        return tree[tree_idx]
    mid = (s + e) // 2
    if mid < fr:
        return find_tree(mid + 1, e, 2 * tree_idx + 1, fr, to)
    elif to <= mid:
        return find_tree(s, mid, 2 * tree_idx, fr, to)
    else:
        return find_tree(s, mid, 2 * tree_idx, fr, mid) + find_tree(mid + 1, e, 2 * tree_idx + 1, mid + 1, to)


def fix_tree(s, e, tree_idx, idx, add):
    if s <= idx <= e:
        tree[tree_idx] += add
        if s != e:
            mid = (s + e) // 2
            if idx <= mid:
                fix_tree(s, mid, 2 * tree_idx, idx, add)
            else:
                fix_tree(mid + 1, e, 2 * tree_idx + 1, idx, add)


make_tree(0, N - 1, 1)

M = int(input())
for _ in range(M):
    c, l, r = map(int, input().split())
    if c == 1:
        l -= 1
        if lst[l] % 2 != r % 2:
            if lst[l] % 2:
                fix_tree(0, N - 1, 1, l, -1)
            else:
                fix_tree(0, N - 1, 1, l, 1)
        lst[l] = r
    elif c == 2:
        l, r = l - 1, r - 1
        print((r - l + 1) - find_tree(0, N - 1, 1, l, r))
    elif c == 3:
        l, r = l - 1, r - 1
        print(find_tree(0, N - 1, 1, l, r))
