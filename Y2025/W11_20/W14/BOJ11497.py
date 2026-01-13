import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    trunk = list(map(int, input().split()))
    trunk.sort()
    max_ = 0
    for i in range(N - 2):
        max_ = max(max_, trunk[i + 2] - trunk[i])
    max_ = max(max_, trunk[1] - trunk[0], trunk[-1] - trunk[-2])
    print(max_)
