import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = []
ans = []
val = 1
for _ in range(n):
    now = int(input())
    while True:
        if not stack:
            stack.append(val)
            ans.append("+")
            val += 1
        if stack[-1] == now:
            ans.append("-")
            stack.pop()
            flag = 0
            break
        stack.append(val)
        ans.append("+")
        val += 1
        if val > n + 1:
            flag = 1
            break
    if flag:
        break

if flag:
    print("NO")
else:
    for i in ans:
        print(i)
