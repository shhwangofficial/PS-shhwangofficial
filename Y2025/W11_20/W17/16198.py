import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))


def dfs(lst, val):
    if len(lst) == 2:
        return val
    now = 0
    for i in range(1, len(lst) - 1):
        now = max(now, dfs(lst[:i] + lst[i + 1 :], val + (lst[i - 1] * lst[i + 1])))
    return now


print(dfs(lst, 0))
