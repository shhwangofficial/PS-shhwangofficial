import sys
from collections import deque

N = int(sys.stdin.readline())
board = []

flag = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    if not flag:
        for j in range(N):
            if row[j] == 9:
                shark_x, shark_y = [i, j]
                flag = 1
                break
    board.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

shark_size = 2
caught = 0
time = 0

while True:
    cands = []
    queue = deque([[shark_x, shark_y, 0]])
    visited = [[0] * N for i in range(N)]
    visited[shark_x][shark_y] = 1
    while queue:
        now_x, now_y, now_d = queue.popleft()
        if 0 < board[now_x][now_y] < shark_size:
            cands.append([now_x, now_y, now_d])
            continue
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if (
                0 <= new_x < N
                and 0 <= new_y < N
                and visited[new_x][new_y] == 0
                and board[new_x][new_y] <= shark_size
            ):
                visited[new_x][new_y] = 1
                queue.append([new_x, new_y, now_d + 1])
    if cands:
        board[shark_x][shark_y] = 0
        cands.sort(key=lambda x: (x[2], x[0], x[1]))
        shark_x, shark_y = cands[0][0], cands[0][1]
        time += cands[0][2]
        board[shark_x][shark_y] = 0
        caught += 1
        if caught == shark_size:
            caught = 0
            shark_size += 1
    else:
        break

print(time)
