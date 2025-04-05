import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)


def make_tree(s, e, tree_idx):
    if s == e:
        sum_tree[tree_idx] = lst[s]
        min_idx_tree[tree_idx] = s
        return (lst[s], s)
    mid = (s + e) // 2
    left = make_tree(s, mid, 2 * tree_idx)
    right = make_tree(mid + 1, e, 2 * tree_idx + 1)
    sum_tree[tree_idx] = left[0] + right[0]
    min_idx_tree[tree_idx] = left[1] if lst[left[1]] <= lst[right[1]] else right[1]
    return (sum_tree[tree_idx], min_idx_tree[tree_idx])


def find_tree(s, e, fr, to, tree_idx):
    if s == e or (s == fr and e == to):
        return (sum_tree[tree_idx], min_idx_tree[tree_idx])

    mid = (s + e) // 2
    if to <= mid:
        return find_tree(s, mid, fr, to, 2 * tree_idx)
    elif mid < fr:
        return find_tree(mid + 1, e, fr, to, 2 * tree_idx + 1)
    else:
        left = find_tree(s, mid, fr, mid, 2 * tree_idx)
        right = find_tree(mid + 1, e, mid + 1, to, 2 * tree_idx + 1)
        real_min_idx = left[1] if lst[left[1]] <= lst[right[1]] else right[1]
        return (left[0] + right[0], real_min_idx)


def find_ans():
    stack = [(0, N - 1)]
    while stack:
        s, e = stack.pop()
        if s > e:
            continue
        sum_, min_idx = find_tree(0, N - 1, s, e, 1)
        global ans
        ans = max(ans, sum_ * lst[min_idx])
        stack.append((s, min_idx - 1))
        stack.append((min_idx + 1, e))


N = int(input())
lst = list(map(int, input().split()))
sum_tree = [0] * (4 * N)
min_idx_tree = [0] * (4 * N)
make_tree(0, N - 1, 1)
ans = 0
find_ans()
print(ans)
