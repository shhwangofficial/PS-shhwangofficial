import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]

goals = set([])
for r in range(row):
    for c in range(col):
        if board[r][c] == "0":
            sr, sc = r, c
        elif board[r][c] == "1":
            goals.add((r, c))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[[0] * (col) for _ in range(row)] for i in range(64 + 1)]
visited[0][sr][sc] = 1
queue = deque([(sr, sc, 0, 0)])
while queue:
    r, c, t, key = queue.popleft()
    if (r, c) in goals:
        print(t)
        exit()

    for d in range(4):
        nr, nc = r + dx[d], c + dy[d]
        if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != "#":
            if "A" <= board[nr][nc] <= "F" and not (1 << (ord(board[nr][nc]) - 65) & key):
                continue
            if visited[key][nr][nc] != 1:
                visited[key][nr][nc] = 1
                if "a" <= board[nr][nc] <= "f":
                    queue.append((nr, nc, t + 1, key | (1 << (ord(board[nr][nc])) - 97)))
                else:
                    queue.append((nr, nc, t + 1, key))

print(-1)
