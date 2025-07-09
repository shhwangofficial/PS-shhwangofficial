import sys

m = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[0] * (m + 1) for _ in range(19)]
graph[0] = num

for r in range(1, 19):
    for c in range(1, m + 1):
        graph[r][c] = graph[r - 1][graph[r - 1][c]]

Q = int(sys.stdin.readline())
for _ in range(Q):
    n, x = map(int, sys.stdin.readline().split())
    ans = x
    for i in range(19):
        if n & (1 << i):
            ans = graph[i][ans]
    print(ans)
