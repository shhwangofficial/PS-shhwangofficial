import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

graph = []
visited = []
visited_broken = []

for i in range(row):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    visited.append([0 for j in range(col)])
    visited_broken.append([0 for j in range(col)])

visited[0][0] = 1
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
walled = 0
dist = 1
queue = deque([[0, 0, walled, dist]])

while queue:
    now = queue.popleft()

    if now[0] == row - 1 and now[1] == col - 1:
        print(now[3])
        sys.exit(0)
    for i in range(0, 4):
        new_x = now[0] + dx[i]
        new_y = now[1] + dy[i]
        new_dist = now[3] + 1
        if 0 <= (new_x) <= row - 1 and 0 <= (new_y) <= col - 1:
            if now[2] == 0:  # 한번도 벽을 뚫지 않고 왔다면
                if graph[new_x][new_y] == 1:  # 벽이라면 한번만 뚫기
                    visited_broken[new_x][new_y] = 1
                    queue.append([new_x, new_y, 1, new_dist])
                else:
                    if visited[new_x][new_y] == 0:
                        visited[new_x][new_y] = 1
                        queue.append([new_x, new_y, now[2], new_dist])
            else:  # 한번 벽을 뚫고 왔다면
                if graph[new_x][new_y] == 0:  # 벽이 아니어야하고
                    if (
                        visited_broken[new_x][new_y] == 0
                    ):  # 벽은 뚫은 채로 방문한 적이 없어야함
                        visited_broken[new_x][new_y] = 1
                        queue.append([new_x, new_y, now[2], new_dist])

print(-1)
