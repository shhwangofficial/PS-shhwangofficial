import sys
N = int(sys.stdin.readline())
max_list = [0, 0, 0]
min_list = [0, 0, 0]
for _ in range(N):
    next_line = list(map(int, sys.stdin.readline().split()))
    next_line_max = [_ for _ in next_line]
    next_line_max[0] += max(max_list[0], max_list[1])
    next_line_max[1] += max(max_list)
    next_line_max[2] += max(max_list[1], max_list[2])
    max_list = next_line_max

    next_line_min = [_ for _ in next_line]
    next_line_min[0] += min(min_list[0], min_list[1])
    next_line_min[1] += min(min_list)
    next_line_min[2] += min(min_list[1], min_list[2])
    min_list = next_line_min

print(max(max_list), min(min_list))