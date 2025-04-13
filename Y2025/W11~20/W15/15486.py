import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict

N = int(input())
now = 0
dic = defaultdict(int)

for i in range(1, N + 1):
    T, P = map(int, input().split())
    now = max(now, dic[i])
    dic[T + i] = max(dic[T + i], now + P)

print(max(now, dic[N + 1]))
