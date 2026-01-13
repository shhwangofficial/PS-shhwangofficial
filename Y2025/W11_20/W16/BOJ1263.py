import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    T, S = map(int, input().split())
    lst.append((T, S))
lst.sort(key=lambda x: -x[1])
now = lst[0][1]
for T, S in lst:
    now = min(now, S)
    now -= T
print(now if now >= 0 else -1)
