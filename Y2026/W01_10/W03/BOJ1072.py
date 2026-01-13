import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

X, Y = map(int, input().split())

original = int(Y * 100 / X)

add = -1
s, e = 1, 1000000000
while s <= e:
    mid = (s + e) // 2
    if int((Y + mid) * 100 / (X + mid)) != original:
        add = mid
        e = mid - 1
    else:
        s = mid + 1

print(add)
