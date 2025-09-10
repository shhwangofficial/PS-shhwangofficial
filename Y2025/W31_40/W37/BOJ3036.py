import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))

from math import gcd

for i in range(1, N):
    val = gcd(lst[0], lst[i])
    print(f"{lst[0]//val}/{lst[i]//val}")
