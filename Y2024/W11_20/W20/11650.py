import sys

N = int(sys.stdin.readline())
dots = []
for i in range(N):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(*dots[i])
