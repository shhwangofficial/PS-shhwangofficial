import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, H = map(int, input().split())

rise = [0] * H
fall = [0] * H
for i in range(N):
    lev = int(input())
    if i % 2:
        fall[H - lev] += 1
    else:
        rise[lev - 1] += 1

total = [0] * H
add = 0
for i in range(H - 1, -1, -1):
    add += rise[i]
    total[i] += add
add = 0
for i in range(H):
    add += fall[i]
    total[i] += add

min_ = float("inf")
cnt = 0
for i in range(H):
    if total[i] < min_:
        min_ = total[i]
        cnt = 1
    elif total[i] == min_:
        cnt += 1

print(min_, cnt)
