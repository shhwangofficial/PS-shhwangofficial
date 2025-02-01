import sys

N = int(sys.stdin.readline())
stack = []
ans = 0
for i in range(N):
    num = int(sys.stdin.readline())
    while stack and stack[-1] < num:
        stack.pop()
        ans += 1
    if stack:
        ans += 1
    stack.append(num)

print(ans)
