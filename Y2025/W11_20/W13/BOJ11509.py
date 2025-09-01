import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict

N = int(input())
balloons = list(map(int, input().split()))
arrows = defaultdict(int)
arr_cnt = 0
for balloon in balloons:
    if arrows[balloon]:
        arrows[balloon] -= 1
    else:
        arr_cnt += 1
    arrows[balloon - 1] += 1
print(arr_cnt)
