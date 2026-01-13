import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, M = map(int, input().split())
sr, sc, tr, tc = map(lambda x: int(x) - 1, input().split())

board = [list(map(str, input())) for _ in range(N)]


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

t = 0
while True:
    t += 1
    queue = deque([(sr, sc)])
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    while queue:
        r, c = queue.popleft()
        if r == tr and c == tc:
            print(t)
            exit()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if board[nr][nc] == "1":
                    board[nr][nc] = "0"
                    visited[nr][nc] = 1
                else:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
