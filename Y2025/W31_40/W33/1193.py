import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

X = int(input())
cnt = [1]
add = 1
while True:
    if cnt[-1] >= X:
        i = len(cnt) - 1
        break
    add += 1
    cnt.append(cnt[-1] + add)

r = cnt[i] - X
c = i - (cnt[i] - X)
if i % 2:
    r, c = c, r
print(f"{r+1}/{c+1}")
