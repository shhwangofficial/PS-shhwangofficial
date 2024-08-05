import sys
from collections import deque

row_max, col_max = map(int, sys.stdin.readline().split())
graph = []

for _ in range(row_max):
    graph.append(list(map(int, sys.stdin.readline().split())))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
time = 0
prev = 0
for i in range(row_max):
    for j in range(col_max):
        if graph[i][j] == 1:
            prev += 1
while True:
    visited = [[0] * col_max for i in range(row_max)]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        now = queue.popleft()
        for i in range(4):
            new_x = now[0] + dx[i]
            new_y = now[1] + dy[i]
            if 0 <= new_x < row_max and 0 <= new_y < col_max:
                if graph[new_x][new_y] == 0:
                    if visited[new_x][new_y] == 0:
                        visited[new_x][new_y] += 1
                        queue.append((new_x, new_y))
                elif graph[new_x][new_y] == 1:
                    visited[new_x][new_y] += 1
    for i in range(row_max):
        for j in range(col_max):
            if graph[i][j] == 1 and visited[i][j] >= 1:
                graph[i][j] = 0
    time += 1
    cnt = 0
    for i in range(row_max):
        for j in range(col_max):
            if graph[i][j] == 1:
                cnt += 1

    if cnt == 0:
        print(time)
        print(prev)
        exit()
    prev = cnt
