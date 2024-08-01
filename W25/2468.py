import sys
from collections import deque
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heights = set()
for i in range(N):
    for j in range(N):
        heights.add(board[i][j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_island = 1
for height in heights:
    visited = [[0]*(N) for i in range(N)]
    island = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > height and visited[i][j] == 0:
                island += 1
                visited[i][j] = 1
                queue = deque([[i, j]])
                while queue:
                    now = queue.popleft()
                    for k in range(4):
                        new_x = now[0] + dx[k]
                        new_y = now[1] + dy[k]
                        if 0<=new_x<N and 0<=new_y<N:
                            if board[new_x][new_y] > height and visited[new_x][new_y] == 0:
                                visited[new_x][new_y] = 1
                                queue.append([new_x, new_y])
    if island > max_island:
        max_island = island

print(max_island)



