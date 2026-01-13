import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    tmp = lst[-1]
    ans = 0
    for i in range(N - 1, -1, -1):
        if lst[i] > tmp:
            tmp = lst[i]
        ans += tmp - lst[i]

    print(ans)
