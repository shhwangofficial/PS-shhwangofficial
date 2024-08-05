import sys

T = int(sys.stdin.readline())
A = int(sys.stdin.readline())
A_lst = list(map(int, sys.stdin.readline().split()))
B = int(sys.stdin.readline())
B_lst = list(map(int, sys.stdin.readline().split()))

B_dict = {}

for i in range(B):
    k = 0
    for j in range(i, B):
        k += B_lst[j]
        B_dict[k] = B_dict.get(k, 0) + 1
cnt = 0
for i in range(A):
    k = 0
    for j in range(i, A):
        k += A_lst[j]
        cnt += B_dict.get(T - k, 0)

print(cnt)
