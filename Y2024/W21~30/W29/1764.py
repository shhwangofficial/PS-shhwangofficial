import sys

a, b = map(int, sys.stdin.readline().split())

set_A = set()
set_B = set()

for i in range(a):
    set_A.add(sys.stdin.readline().rstrip())
for i in range(b):
    set_B.add(sys.stdin.readline().rstrip())

set_A = set_A.intersection(set_B)
set_A = sorted(list(set_A))
print(len(set_A))

for i in set_A:
    print(i)
