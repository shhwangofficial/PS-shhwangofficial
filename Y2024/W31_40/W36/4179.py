import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [[10**6] * C for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
fires = []
for i in range(R):
    for j in range(C):
        if board[i][j] == "J":
            rJ, cJ = i, j
        if board[i][j] == "F":
            fires.append([i, j])
            visited[i][j] = 0

queueFire = deque([[0] + fire for fire in fires])
while queueFire:
    time, r, c = queueFire.popleft()
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == "#":
                continue
            if visited[nr][nc] > time + 1:
                visited[nr][nc] = time + 1
                queueFire.append([time + 1, nr, nc])

queueJ = deque([[0, rJ, cJ]])
while queueJ:
    time, r, c = queueJ.popleft()
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == "#":
                continue
            if time + 1 < visited[nr][nc]:
                visited[nr][nc] = 0
                queueJ.append([time + 1, nr, nc])
        else:
            print(time + 1)
            exit()
print("IMPOSSIBLE")
