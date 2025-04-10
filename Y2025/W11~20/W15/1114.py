import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

L, K, C = map(int, input().split())
positions = list(set(list(map(int, input().split()))))
positions.sort()

s, e = 1, L
ans = -1
ans_edge = -1
while s <= e:
    edge = L
    now_cut = (s + e) // 2
    flag = 0
    cut_count = 0
    while True:
        find = edge - now_cut
        small_s = 0
        small_e = len(positions) - 1
        temp = -1
        while small_s <= small_e:
            mid_index = (small_s + small_e) // 2
            if find <= positions[mid_index]:
                temp = mid_index
                small_e = mid_index - 1
            else:
                small_s = mid_index + 1
        if temp == -1:
            flag = 1
            break
        edge = positions[temp]
        cut_count += 1
        if cut_count > C:
            flag = 1
            break
        if edge - now_cut <= 0 and cut_count == C:
            break
    if flag:
        s = now_cut + 1
    else:
        ans = now_cut
        ans_edge = edge
        e = now_cut - 1


print(ans, ans_edge)
