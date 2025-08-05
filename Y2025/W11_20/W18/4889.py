import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

t = 0
while True:
    line = input()
    if "-" in line:
        break
    t += 1
    stack = []
    ans = 0
    for i in line:
        if i == "}":
            if not stack:
                ans += 1
                stack.append("{")
            else:
                stack.pop()
        elif i == "{":
            stack.append("{")

    ans += len(stack) // 2
    print(f"{t}. {ans}")
