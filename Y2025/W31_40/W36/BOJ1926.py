import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
cnt = 0
max_size = 0
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
for r in range(n):
    for c in range(m):
        if visited[r][c] == 0 and board[r][c] == 1:
            queue = deque([(r, c)])
            visited[r][c] = 1
            cnt += 1
            size = 0
            while queue:
                nowr, nowc = queue.popleft()
                size += 1
                for d in range(4):
                    nr, nc = nowr + dr[d], nowc + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and board[nr][nc] == 1:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
            max_size = max(size, max_size)
print(cnt)
print(max_size)
