import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums_idx = sorted([[nums[i], i] for i in range(N)], key=lambda x: (x[0], x[1]))
tree = [0] * (4 * N)


def get_seg_tree(s, e, idx, fr, to):
    if s == fr and e == to:
        return tree[idx]
    mid = (s + e) // 2
    if fr > mid:
        return get_seg_tree(mid + 1, e, 2 * idx + 1, fr, to)
    elif to <= mid:
        return get_seg_tree(s, mid, 2 * idx, fr, to)
    else:
        return get_seg_tree(s, mid, 2 * idx, fr, mid) + get_seg_tree(mid + 1, e, 2 * idx + 1, mid + 1, to)


def fix_seg_tree(s, e, idx, fr):
    tree[idx] += 1
    if s == e:
        return
    mid = (s + e) // 2
    if fr > mid:
        fix_seg_tree(mid + 1, e, 2 * idx + 1, fr)
    elif fr <= mid:
        fix_seg_tree(s, mid, 2 * idx, fr)


ans = 0
prev = nums_idx[0][0] - 1
temp = 0
for num, idx in nums_idx:

    if num != prev:
        temp = get_seg_tree(0, N - 1, 1, idx + 1, N - 1)
    ans += temp
    fix_seg_tree(0, N - 1, 1, idx)
    prev = num

print(ans)
