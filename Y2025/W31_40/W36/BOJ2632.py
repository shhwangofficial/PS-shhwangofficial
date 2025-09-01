import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict

want = int(input())
m, n = map(int, input().split())
A, B = [], []

for _ in range(m):
    A.append(int(input()))
for _ in range(n):
    B.append(int(input()))

A_dict = defaultdict(int)
B_dict = defaultdict(int)

for i in range(m):
    A_dict[A[i]] += 1
    sum_ = A[i]
    now_idx = (i + 1) % m
    while now_idx != i:
        sum_ += A[now_idx]
        A_dict[sum_] += 1
        now_idx = (now_idx + 1) % m
for i in range(n):
    B_dict[B[i]] += 1
    sum_ = B[i]
    now_idx = (i + 1) % n
    while now_idx != i:
        sum_ += B[now_idx]
        B_dict[sum_] += 1
        now_idx = (now_idx + 1) % n

A_dict[sum(A)] = 1
B_dict[sum(B)] = 1
A_dict[0] = 1
B_dict[0] = 1

ans = 0
for i in range(want + 1):
    j = want - i
    ans += A_dict[i] * B_dict[j]

print(ans)
