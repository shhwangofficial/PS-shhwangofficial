import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
inf = 10**7
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

v_day = [[[inf] * (K + 1) for _ in range(M)] for i in range(N)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque([[0, 0, 1, 0, True]])
v_day[0][0][0] = 1

while queue:
    r, c, t, w, dn = queue.popleft()
    if r == N - 1 and c == M - 1:
        continue

    add = 0
    for i in range(4):
        nr, nc, nt = r + dx[i], c + dy[i], t + 1
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 1 and dn:
                nw = w + 1
            elif board[nr][nc] == 1 and not dn:
                add = 1
                continue
            else:
                nw = w
            if nw <= K and v_day[nr][nc][nw] > nt:
                v_day[nr][nc][nw] = nt
                queue.append([nr, nc, nt, nw, not dn])

    if dn == False and add == 1:
        queue.append([r, c, nt, w, not dn])


ans = inf
for W in range(K + 1):
    ans = min(ans, v_day[N - 1][M - 1][W])

print(-1 if ans == inf else ans)
