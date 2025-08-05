import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
board = []

info = [[0] * (N * N) for _ in range(N * N)]
houses = []
chickens = []
for i in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    board.append(num)
    for j in range(N):
        if num[j] == 1:
            houses.append(i * N + j)
        if num[j] == 2:
            chickens.append(i * N + j)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for house in houses:
    r, c = house // N, house % N
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    queue = deque([[r, c, 0]])
    while queue:
        qr, qc, qd = queue.popleft()
        if board[qr][qc] == 2:
            info[house][qr * N + qc] = qd
        for i in range(4):
            nr, nc = qr + dx[i], qc + dy[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append([nr, nc, qd + 1])

ans = 99999
for comb in combinations(chickens, M):
    sum_ = 0
    for house in houses:
        dist = 99999
        for chick in comb:
            dist = min(dist, info[house][chick])
        sum_ += dist
    ans = min(ans, sum_)

print(ans)
