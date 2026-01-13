import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

val = 0
for i in range(1, N + 1):
    val = (val + K) % i

print(val + 1)
