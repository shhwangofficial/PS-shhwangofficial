import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))


def solve():
    for i in range(N - 2, -1, -1):
        if lst[i] < lst[i + 1]:
            for j in range(N - 1, i, -1):
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    lst[i + 1 :] = sorted(lst[i + 1 :])
                    print(*lst)

                    return
    print(-1)


solve()
