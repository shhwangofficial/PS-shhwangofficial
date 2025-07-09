import sys

N = int(sys.stdin.readline()) - 1

for i in range(N, -1, -1):
    for j in range(i):
        print(" ", end="")
    for s in range(2 * (N - i) + 1):
        print("*", end="")
    print()

for i in range(1, N + 1):
    for j in range(i):
        print(" ", end="")
    for s in range(2 * (N - i) + 1):
        print("*", end="")
    print()
