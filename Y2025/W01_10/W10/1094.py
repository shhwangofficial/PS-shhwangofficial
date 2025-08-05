import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

cnt = 0
for i in range(6):
    if N & (1 << i):
        cnt += 1

print(max(cnt, 1))
