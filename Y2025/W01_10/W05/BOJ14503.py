import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0
queue = deque([(r, c, d)])
while queue:
    r, c, d = queue.popleft()
    if visited[r][c] == 0:
        visited[r][c] = 1
        ans += 1
    for i in range(1, 4 + 1):
        nr, nc, nd = r + dy[d - i], c + dx[d - i], (d - i) % 4
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc] == 0 and board[nr][nc] == 0:
                queue.append((nr, nc, nd))
                break
    else:
        nr, nc, nd = r + dy[d - 2], c + dx[d - 2], d
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
            queue.append((nr, nc, nd))
        else:
            break

print(ans)
