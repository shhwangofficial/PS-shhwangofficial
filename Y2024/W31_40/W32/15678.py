import sys
import math

N, D = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

segtree = [-math.inf] * (4 * N)
dp = [0] * N


def find_max(from_, to_, start, end, idx):
    if start == from_ and end == to_:
        return segtree[idx]
    mid = (start + end) // 2
    if to_ <= mid:
        return find_max(from_, to_, start, mid, idx * 2)
    elif from_ > mid:
        return find_max(from_, to_, mid + 1, end, idx * 2 + 1)
    else:
        return max(
            find_max(from_, mid, start, mid, idx * 2),
            find_max(mid + 1, to_, mid + 1, end, idx * 2 + 1),
        )


def fix_tree(idx_val, val, start, end, idx_tree):
    segtree[idx_tree] = max(segtree[idx_tree], val)
    if start == end:
        return
    mid = (start + end) // 2
    if idx_val <= mid:
        fix_tree(idx_val, val, start, mid, idx_tree * 2)
    else:
        fix_tree(idx_val, val, mid + 1, end, idx_tree * 2 + 1)


for i in range(N):
    max_ = find_max(max(0, i - D), i, 0, N - 1, 1)
    if max_ == -math.inf:
        dp[i] = nums[i]
    else:
        dp[i] = max(max_ + nums[i], nums[i])
    fix_tree(i, dp[i], 0, N - 1, 1)

print(find_max(0, N - 1, 0, N - 1, 1))
