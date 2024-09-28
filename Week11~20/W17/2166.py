import sys

N = int(sys.stdin.readline())
dots = []
for _ in range(N):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.append(dots[0])

sum_area = 0
for i in range(N):
    sum_area += dots[i][0] * dots[i + 1][1]
    sum_area -= dots[i][1] * dots[i + 1][0]

print(round(abs(sum_area) / 2, 1))
