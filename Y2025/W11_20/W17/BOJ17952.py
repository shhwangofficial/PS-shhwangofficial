import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stack = []
ans = 0
for _ in range(N):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        stack.append([lst[1], lst[2]])
    if stack:
        stack[-1][1] -= 1
        if stack[-1][1] == 0:

            ans += stack.pop()[0]
print(ans)
