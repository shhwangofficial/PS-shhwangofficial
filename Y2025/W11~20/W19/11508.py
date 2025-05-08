import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
milk = [int(input()) for _ in range(N)]
milk.sort(reverse=True)

free = 0
for i in range(2, N, 3):
    free += milk[i]

print(sum(milk) - free)
