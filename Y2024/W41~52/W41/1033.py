import sys
from math import gcd, lcm

N = int(sys.stdin.readline())
if N == 1:
    print(1)
    exit()
graph = [[0] * N for _ in range(N - 1)]

for i in range(N - 1):
    a, b, c, d = map(int, sys.stdin.readline().split())
    div = gcd(c, d)
    graph[i][a], graph[i][b] = c // div, d // div

for u in range(N):
    for i in range(N - 1):
        for j in range(N - 1):
            up, down = 0, 0
            for k in range(N):
                if graph[i][k] > 0 and graph[j][k] > 0:
                    up, down = graph[i][k], graph[j][k]
                    break
            if up * down:
                lcm_ = lcm(up, down)
                up_x, down_x = lcm_ // up, lcm_ // down
                for k in range(N):
                    graph[i][k] *= up_x
                    graph[j][k] *= down_x

ans = [0] * N
for i in range(N - 1):
    for j in range(N):
        if graph[i][j] > 0:
            ans[j] = graph[i][j]

print(*ans)
