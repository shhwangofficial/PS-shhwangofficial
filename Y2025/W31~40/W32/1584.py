import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappop, heappush

board = [[0] * 501 for _ in range(501)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            board[x][y] = 1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            board[x][y] = -1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
heap = [(0, 0, 0)]
visited = [[0] * 501 for _ in range(501)]
distance = [[float("inf")] * 501 for _ in range(501)]
distance[0][0] = 0
while heap:
    d, x, y = heappop(heap)
    if visited[x][y]:
        continue
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 500 and 0 <= ny <= 500 and visited[nx][ny] == 0 and board[nx][ny] != -1:
            if distance[nx][ny] > d + board[nx][ny]:
                distance[nx][ny] = d + board[nx][ny]
                heappush(heap, (distance[nx][ny], nx, ny))

if distance[500][500] == float("inf"):
    print(-1)
else:
    print(distance[500][500])
