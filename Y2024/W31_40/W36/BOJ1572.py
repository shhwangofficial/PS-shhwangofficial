import sys

N, K = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]

seg_tree = [0] * (4 * 65536)


def insert_num(start, end, val, tree_idx):
    seg_tree[tree_idx] += 1
    if start == end:
        return
    mid = (start + end) // 2
    if mid < val:
        insert_num(mid + 1, end, val, 2 * tree_idx + 1)
    else:
        insert_num(start, mid, val, 2 * tree_idx)


def delete_num(start, end, val, tree_idx):
    seg_tree[tree_idx] -= 1
    if start == end:
        return
    mid = (start + end) // 2
    if mid < val:
        delete_num(mid + 1, end, val, 2 * tree_idx + 1)
    else:
        delete_num(start, mid, val, 2 * tree_idx)


def find_median(start, end, nth, tree_idx):
    if start == end:
        return start
    left = seg_tree[2 * tree_idx]
    mid = (start + end) // 2
    if left >= nth:
        return find_median(start, mid, nth, 2 * tree_idx)
    else:
        nth -= left
        return find_median(mid + 1, end, nth, 2 * tree_idx + 1)


for i in range(K - 1):
    insert_num(0, 65536, nums[i], 1)

sum_ = 0
for i in range(N - K + 1):
    insert_num(0, 65536, nums[i + K - 1], 1)
    sum_ += find_median(0, 65536, (K + 1) // 2, 1)
    delete_num(0, 65536, nums[i], 1)

print(sum_)
