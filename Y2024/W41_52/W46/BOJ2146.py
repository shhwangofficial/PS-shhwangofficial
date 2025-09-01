import sys
from collections import deque

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[-1] * N for _ in range(N)]

island = [-1] * (N * N)

island_no = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and visited[r][c] == -1:
            island_no += 1
            visited[r][c] = 0
            queue = deque([(r, c)])
            island[r * N + c] = island_no
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nr, nc = x + dx[i], y + dy[i]
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1 and board[nr][nc] == 1:
                        visited[nr][nc] = 0
                        island[nr * N + nc] = island_no
                        queue.append((nr, nc))

step = 0
ans = 999
flag = 0
while True:
    for r in range(N):
        for c in range(N):
            if visited[r][c] == step:
                for i in range(4):
                    nr, nc = r + dx[i], c + dy[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if visited[nr][nc] == -1:
                            visited[nr][nc] = step + 1
                            island[nr * N + nc] = island[r * N + c]
                        elif island[nr * N + nc] != island[r * N + c]:
                            ans = min(step + visited[nr][nc], ans)
                            flag = 1
    if flag:
        print(ans)
        exit()

    step += 1
