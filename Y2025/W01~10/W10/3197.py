import sys

sys.stdin = open("python_input.txt", "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

R, C = map(int, input().split())
board = [input() for _ in range(R)]

swan = deque([])
next_day_swan = deque([])
water = deque([])
next_day_water = []

visited_swan = [[[0] * C for _ in range(R)] for s in range(2)]
visited_water = [[0] * C for _ in range(R)]

no_swan = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == "L":
            next_day_swan.append((r, c, no_swan))
            visited_swan[no_swan][r][c] = 1
            water.append((r, c))
            no_swan += 1
        if board[r][c] == ".":
            water.append((r, c))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


flag = 0
day = 1
ans = float("inf")
while True:
    while next_day_swan:
        swan.append(next_day_swan.popleft())
    while swan:
        r, c, no_swan = swan.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and visited_swan[no_swan][nr][nc] == 0:
                if visited_swan[(no_swan + 1) % 2][nr][nc] or board[nr][nc] == "L":
                    flag = 1
                    ans = min(visited_swan[(no_swan + 1) % 2][nr][nc] - 1, ans)
                elif board[nr][nc] == "X":
                    visited_swan[no_swan][nr][nc] = day + 1
                    next_day_swan.append((nr, nc, no_swan))
                elif board[nr][nc] == ".":
                    visited_swan[no_swan][nr][nc] = day
                    swan.append((nr, nc, no_swan))

    if flag:
        break

    while water:
        r, c = water.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and visited_water[nr][nc] == 0:
                visited_water[nr][nc] = 1
                if board[nr][nc] == "X":
                    next_day_water.append((nr, nc))
                elif board[nr][nc] == ".":
                    water.append((nr, nc))

    for wr, wc in next_day_water:
        board[wr] = board[wr][:wc] + "." + board[wr][wc + 1 :]
        water.append((wr, wc))

    next_day_water = []

    day += 1

print(max(0, ans))
