import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
visited = set([])


def recur(lst):
    if len(lst) == N:
        print(*lst)
        return

    for i in range(1, N + 1):
        if i not in visited:
            visited.add(i)
            recur(lst + [i])
            visited.discard(i)


recur([])
