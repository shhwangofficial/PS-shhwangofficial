import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lst = list(map(int, input().split()))

tree = [0] * (4 * n)


def find_tree(s, e, idx, val):
    if s == e:
        tree[idx] += 1
        return tree[idx] - 1
    mid = (s + e) // 2
    if mid < val:
        ret = find_tree(mid + 1, e, 2 * idx + 1, val)
    else:
        ret = find_tree(s, mid, 2 * idx, val) + tree[2 * idx + 1]
    tree[idx] += 1
    return ret


ans = 0
for i in range(len(lst) - 1, -1, -1):
    val = lst[i]
    ans += n - val - find_tree(1, n, 1, val)

print(ans)
