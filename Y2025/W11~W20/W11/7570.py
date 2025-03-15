import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
kids = list(map(int, input().split()))
len_list = [0] * (N + 1)
for kid in kids:
    len_list[kid] = len_list[kid - 1] + 1

print(N - max(len_list))
