import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [input() for _ in range(R)]
dr = [1, 1]
dc = [-1, 1]


def proceed(r, c, d):
    visited[d][r][c] = 1
    nowr, nowc, step = r, c, 1
    while True:
        nr, nc, nstep = nowr + dr[d], nowc + dc[d], step + 1
        if 0 <= nr < R and 0 <= nc < C and visited[d][nr][nc] == 0 and board[nr][nc] == "1":
            visited[d][nr][nc] = nstep
            nowr, nowc, step = nr, nc, nstep
        else:
            break


visited = [[[0] * C for _ in range(R)] for _ in range(2)]
for r in range(R):
    for c in range(C):
        if board[r][c] == "1":
            if visited[0][r][c] == 0:
                proceed(r, c, 0)
            if visited[1][r][c] == 0:
                proceed(r, c, 1)

tmp_max = 0
for r in range(R):
    for c in range(C):
        if visited[0][r][c] >= 1 and visited[1][r][c] >= 1:
            tmp_max = max(1, tmp_max)
            tmp_size = min(visited[0][r][c], visited[1][r][c])
            for k in range(tmp_size, tmp_max, -1):
                leftr, leftc = r - (k - 1), c - (k - 1)
                rightr, rightc = r - (k - 1), c + (k - 1)
                if visited[0][leftr][leftc] >= k and visited[1][rightr][rightc] >= k:
                    tmp_max = max(tmp_max, k)

print(tmp_max)
