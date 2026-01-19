import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == "L":
            temp = 0
            visited = [[0] * C for i in range(R)]
            visited[r][c] = 1
            queue = deque([(0, r, c)])
            while queue:
                d, x, y = queue.popleft()
                temp = max(d, temp)
                for i in range(4):
                    nr, nc = x + dr[i], y + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and board[nr][nc] == "L":
                        visited[nr][nc] = 1
                        queue.append((d + 1, nr, nc))
            ans = max(ans, temp)


print(ans)
