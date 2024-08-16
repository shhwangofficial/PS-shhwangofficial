import sys

sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

index_lst = [0] * (N + 1)
for i in range(len(in_order)):
    index_lst[in_order[i]] = i


def splitting(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    print(post_order[post_end])
    new_end = index_lst[post_order[post_end]]
    splitting(in_start, new_end - 1, post_start, post_start + (new_end - 1 - in_start))
    splitting(new_end + 1, in_end, (post_end - 1) - (in_end - (new_end + 1)), post_end - 1)


splitting(0, N - 1, 0, N - 1)
