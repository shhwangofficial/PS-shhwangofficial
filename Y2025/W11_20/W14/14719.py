import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
blocks = list(map(int, input().split()))


rain = 0

for h in range(H):
    stack = []
    for b in range(W):
        if blocks[b] > h:
            if stack:
                rain += b - stack.pop() - 1
            stack.append(b)

print(rain)
