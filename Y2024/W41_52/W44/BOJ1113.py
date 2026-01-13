import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
for r in range(1, N - 1):
    for c in range(1, M - 1):
        visited[r][c] = 1
        queue = deque([(r, c)])
        lev = board[r][c]
        visited_lst = [(r, c)]
        max_wall = 9
        leak_to_groud = 0
        while queue:
            if leak_to_groud:
                break
            qr, qc = queue.popleft()
            for i in range(4):
                nr, nc = qr + dx[i], qc + dy[i]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                    if nr == 0 or nr == N - 1 or nc == 0 or nc == M - 1:
                        if board[nr][nc] <= lev:
                            leak_to_groud = 1
                            break
                    elif board[nr][nc] <= lev:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
                        visited_lst.append((nr, nc))
                    if board[nr][nc] > lev:
                        max_wall = min(max_wall, board[nr][nc])

        for x, y in visited_lst:
            if not leak_to_groud:
                ans += max_wall - (board[x][y])
                board[x][y] = max_wall
            visited[x][y] = 0

print(ans)
