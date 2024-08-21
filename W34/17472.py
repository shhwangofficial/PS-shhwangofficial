import sys
import heapq

rows, cols = map(int, sys.stdin.readline().split())
board = []
visited = [[0] * cols for _ in range(rows)]
for _ in range(rows):
    board.append(list(map(int, sys.stdin.readline().split())))
graph = [[0] * 7 for _ in range(7)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
island_no = 0
for i in range(rows):
    for j in range(cols):
        if board[i][j] == 1 and visited[i][j] == 0:
            island_no += 1
            visited[i][j] = island_no
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] == 0 and board[nx][ny] == 1:
                        visited[nx][ny] = island_no
                        stack.append((nx, ny))

for i in range(rows):
    for j in range(cols):
        if visited[i][j] != 0:
            now_island = visited[i][j]
            for k in range(4):
                inc = 0
                res = 0
                x, y = i + dx[k], j + dy[k]
                while 0 <= x < rows and 0 <= y < cols:
                    if visited[x][y] != 0:
                        if visited[x][y] == now_island:
                            break
                        else:
                            res = inc
                            des = visited[x][y]
                            break
                    else:
                        inc += 1
                        x, y = x + dx[k], y + dy[k]
                if res > 1:
                    if graph[now_island][des] > 0:
                        graph[now_island][des] = min(graph[now_island][des], res)
                    else:
                        graph[now_island][des] = res

connected = [0 for i in range(7)]
heap = [[0, 1]]
sum_ = 0
num_lines = 0
while heap:
    now = heapq.heappop(heap)
    if connected[now[1]] == 0:
        connected[now[1]] = 1
        sum_ += now[0]
        if num_lines == island_no - 1:
            break
        for i in range(len(graph[now[1]])):
            if graph[now[1]][i] > 0:
                if connected[i] == 0:
                    heapq.heappush(heap, [graph[now[1]][i], i])

for i in range(1, island_no + 1):
    if connected[i] == 0:
        print(-1)
        break
else:
    print(sum_)
