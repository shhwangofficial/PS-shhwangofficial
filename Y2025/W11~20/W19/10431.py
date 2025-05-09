import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for t in range(1, N + 1):
    no, *seq = map(int, input().split())
    line = []
    ans = 0
    for s in seq:
        for i in range(len(line)):
            if line[i] > s:
                ans += 1
        line.append(s)
    print(f"{t} {ans}")
