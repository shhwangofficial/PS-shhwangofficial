import sys

N = int(sys.stdin.readline())
lst_a = []
lst_b = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst_a.append(a)
    lst_b.append(b)
lst_a.sort()
lst_b.sort()
if lst_a[-1] - lst_b[0] < 0:
    print(0)
else:
    print(lst_a[-1] - lst_b[0])
