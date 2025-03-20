import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from itertools import permutations
from collections import deque


def bfs(tpl, turn):
    if boards[tpl[0]][turn[0]][0][0] == 0:
        return 0
    visited = [[[0] * N for _ in range(N)] for i in range(N)]
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0, 0)])
    while queue:
        r, c, z, step = queue.popleft()
        if r == N - 1 and c == N - 1 and z == N - 1:
            global ans
            ans = min(ans, step)
            return 1
        for d in range(6):
            nr, nc, nz = r + dr[d], c + dc[d], z + dz[d]
            if 0 <= nr < N and 0 <= nc < N and 0 <= nz < N and visited[nr][nc][nz] == 0:
                if boards[tpl[nz]][turn[nz]][nr][nc] == 1:
                    visited[nr][nc][nz] = 1
                    queue.append((nr, nc, nz, step + 1))
    return 0


def dfs(tpl, lst):
    if len(lst) == N:
        bfs(tpl, lst)
        return
    for i in range(4):
        dfs(tpl, lst + [i])


dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
N = 5
boards = []
for k in range(N):
    b = []
    board = [list(map(int, input().split())) for i in range(N)]
    b.append(board[:])
    for _ in range(3):
        new_board = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_board[j][N - i - 1] = b[-1][i][j]
        b.append(new_board[:])
    boards.append(b[:])

ans = float("inf")
perm = permutations(range(N), N)
for p in perm:
    dfs(p, [])
print(ans if ans != float("inf") else -1)
