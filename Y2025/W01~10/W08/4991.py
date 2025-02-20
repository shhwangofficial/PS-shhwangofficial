import sys
from collections import deque

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    board = [list(map(str, input().rstrip())) for _ in range(h)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    total = 0
    for r in range(h):
        for c in range(w):
            if board[r][c] == "*":
                total += 1
                board[r][c] = str(total)
            elif board[r][c] == "o":
                sr, sc = r, c

    queue = deque([(sr, sc, 0, 0)])
    visited = [[[float("inf")] * w for _ in range(h)] for m in range((1 << total) - 1)]
    while queue:
        r, c, bit, step = queue.popleft()
        flag = 0
        for d in range(4):
            nr, nc, nstep = r + dr[d], c + dc[d], step + 1
            if 0 <= nr < h and 0 <= nc < w and board[nr][nc] != "x":
                if board[nr][nc].isdigit():
                    pos = int(board[nr][nc])
                    nbit = bit | 1 << (pos - 1)
                    if nbit == (1 << total) - 1:
                        print(nstep)
                        flag = 1
                        break
                else:
                    nbit = bit

                if visited[nbit][nr][nc] > nstep:
                    visited[nbit][nr][nc] = nstep
                    queue.append((nr, nc, nbit, nstep))
        if flag:
            break
    else:
        print(-1)
