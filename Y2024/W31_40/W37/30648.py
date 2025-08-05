import sys

a, b = map(int, sys.stdin.readline().split())
R = int(sys.stdin.readline())

visited = [[0] * (R + 1) for _ in range(R + 1)]
visited[a][b] = 1
cnt = 0
while 1:
    cnt += 1
    if a + 1 + b + 1 < R:
        a, b = a + 1, b + 1
    else:
        a, b = a // 2, b // 2
    if visited[a][b] == 1:
        print(cnt)
        break
    else:
        visited[a][b] = 1
