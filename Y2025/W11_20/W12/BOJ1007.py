import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations

T = int(input())
for t in range(T):
    N = int(input())
    dots = [list(map(int, input().split())) for _ in range(N)]
    ans = float("inf")
    for comb in combinations(range(N), N // 2):
        set_to = set(comb)
        set_from = set(range(N)) - set_to
        to_x_sum = 0
        to_y_sum = 0
        from_x_sum = 0
        from_y_sum = 0
        for to in set_to:
            to_x_sum += dots[to][0]
            to_y_sum += dots[to][1]
        for fr in set_from:
            from_x_sum += dots[fr][0]
            from_y_sum += dots[fr][1]
        ans = min(ans, abs(((to_x_sum - from_x_sum) ** 2 + (to_y_sum - from_y_sum) ** 2) ** 0.5))
    print(ans)
