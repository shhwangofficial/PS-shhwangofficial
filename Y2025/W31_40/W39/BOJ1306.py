import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
tree = [0] * (4 * N)


def build_tree(s, e, i):
    if s == e:
        tree[i] = lst[s]
        return tree[i]
    mid = (s + e) // 2
    left = build_tree(s, mid, 2 * i)
    right = build_tree(mid + 1, e, 2 * i + 1)
    tree[i] = max(left, right)
    return tree[i]


def find_tree(s, e, fr, to, i):
    if s == fr and e == to:
        return tree[i]
    mid = (s + e) // 2
    if mid < fr:
        return find_tree(mid + 1, e, fr, to, 2 * i + 1)
    elif to <= mid:
        return find_tree(s, mid, fr, to, 2 * i)
    else:
        return max(find_tree(s, mid, fr, mid, 2 * i), find_tree(mid + 1, e, mid + 1, to, 2 * i + 1))


build_tree(0, N - 1, 1)

ans = []
T = M - 1
for i in range(T, N - T):
    ans.append(find_tree(0, N - 1, i - T, i + T, 1))
print(*ans)
