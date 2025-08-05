import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))


def dnc(lst, step):
    if len(lst) == 1:
        ans[step].append(lst[0])
        return
    mid = len(lst) // 2
    ans[step].append(lst[mid])
    dnc(lst[:mid], step + 1)
    dnc(lst[mid + 1 :], step + 1)


ans = [[] for _ in range(N + 1)]
dnc(lst, 1)
for i in range(1, N + 1):
    print(*ans[i])
