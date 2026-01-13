import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()


def propagation(s, e, i, val):
    if s == e:
        lst[s] += val
    else:
        lazy[i] += val


def fix_tree(s, e, i, fr, to, val):
    if s == fr and e == to:
        if s == e:
            lst[s] += val
        else:
            lazy[i] += val
        return
    mid = (s + e) // 2
    if lazy[i]:
        propagation(s, mid, 2 * i, lazy[i])
        propagation(mid + 1, e, 2 * i + 1, lazy[i])
        lazy[i] = 0
    if mid + 1 <= fr:
        fix_tree(mid + 1, e, 2 * i + 1, fr, to, val)
    elif to <= mid:
        fix_tree(s, mid, 2 * i, fr, to, val)
    else:
        fix_tree(s, mid, 2 * i, fr, mid, val)
        fix_tree(mid + 1, e, 2 * i + 1, mid + 1, to, val)


def find_tree(s, e, i, find):
    if s == e == find:
        return lst[s]
    mid = (s + e) // 2
    if lazy[i]:
        propagation(s, mid, 2 * i, lazy[i])
        propagation(mid + 1, e, 2 * i + 1, lazy[i])
        lazy[i] = 0
    if find <= mid:
        return find_tree(s, mid, 2 * i, find)
    else:
        return find_tree(mid + 1, e, 2 * i + 1, find)


N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lazy = [0] * (4 * N)
for _ in range(M):
    comm = list(map(int, input().split()))
    if comm[0] == 1:
        fr, to, val = comm[1] - 1, comm[2] - 1, comm[3]
        fix_tree(0, N - 1, 1, fr, to, val)
    elif comm[0] == 2:
        print(find_tree(0, N - 1, 1, comm[1] - 1))
