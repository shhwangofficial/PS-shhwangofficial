import sys
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[10**5] * 4 for _ in range(N)] for i in range(N)]
flag = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == "#":
            if flag:
                s_r, s_c = i, j
                flag = 0
            else:
                e_r, e_c = i, j

directions = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
queue = deque([])
for i in set(range(4)):
    nr, nc = s_r + directions[i][0], s_c + directions[i][1]
    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "*":
        queue.append([0, nr, nc, i])
        visited[nr][nc][i] = 0


min_ = 10**5
while queue:
    mirrors, r, c, d = queue.popleft()
    if r == e_r and c == e_c:
        min_ = min(min_, mirrors)
        continue
    if board[r][c] == "!":
        for i in set(range(4)) - {d, (d + 2) % 4}:
            nr, nc = r + directions[i][0], c + directions[i][1]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "*":
                if visited[nr][nc][i] > mirrors + 1:
                    visited[nr][nc][i] = mirrors + 1
                    queue.append([mirrors + 1, nr, nc, i])

    nr, nc = r + directions[d][0], c + directions[d][1]
    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "*":
        if visited[nr][nc][d] > mirrors:
            visited[nr][nc][d] = mirrors
            queue.append([mirrors, nr, nc, d])

print(min_)
