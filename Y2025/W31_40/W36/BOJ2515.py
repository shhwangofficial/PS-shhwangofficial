import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())
height_lst = set([0])
cost_dict = dict()
for _ in range(N):
    H, C = map(int, input().split())
    if H in height_lst:
        cost_dict[H] = max(cost_dict[H], C)
    else:
        height_lst.add(H)
        cost_dict[H] = C

height_lst = sorted(list(height_lst))
ans = [0] * len(height_lst)
for i in range(1, len(height_lst)):
    now_height = height_lst[i]
    find_height = max(0, now_height - S)
    s, e = 0, i - 1
    while s <= e:
        mid = (s + e) // 2
        if height_lst[mid] <= find_height:
            tmp = mid
            s = mid + 1
        else:
            e = mid - 1
    ans[i] = max(cost_dict[now_height] + ans[tmp], ans[i - 1])

print(ans[-1])
