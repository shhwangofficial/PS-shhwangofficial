import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))

if N == 1:
    print(sum(lst) - max(lst))
    exit()

threes = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 5, 3), (1, 5, 2), (3, 4, 5), (4, 2, 5)]

twos = [(0, 1), (0, 2), (0, 3), (0, 4), (5, 1), (5, 2), (5, 3), (5, 4), (2, 4), (1, 2), (1, 3), (3, 4)]

two_side = float("inf")
for two in twos:
    tmp = 0
    for t in two:
        tmp += lst[t]
    two_side = min(two_side, tmp)

three_side = float("inf")
for three in threes:
    tmp = 0
    for t in three:
        tmp += lst[t]
    three_side = min(three_side, tmp)

one_side = min(lst)
ans = 4 * three_side + 5 * one_side * ((N - 2) ** 2) + 8 * two_side * (N - 2) + 4 * one_side * (N - 2) + 4 * two_side
print(ans)
