import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque


def roll_red(rr, rc, br, bc, d):
    while True:
        nrr, nrc = rr + dr[d], rc + dc[d]
        if board[nrr][nrc] == "#":
            return rr, rc, br, bc
        elif board[nrr][nrc] == "O":
            return -1, -1, br, bc
        elif nrr == br and nrc == bc:
            br, bc = roll_blue(rr, rc, br, bc, d)
            if br == -1 and bc == -1:
                return -1, -1, -1, -1
            else:
                return br - dr[d], bc - dc[d], br, bc
        else:
            rr, rc = nrr, nrc


def roll_blue(rr, rc, br, bc, d):
    while True:
        nbr, nbc = br + dr[d], bc + dc[d]
        if board[nbr][nbc] == "#":
            return br, bc
        elif board[nbr][nbc] == "O":
            return -1, -1
        elif nbr == rr and nbc == rc:
            return br, bc
        else:
            br, bc = nbr, nbc


N, M = map(int, input().split())
board = [input() for _ in range(N)]
rr, rc, br, bc = 0, 0, 0, 0
for r in range(N):
    for c in range(M):
        if board[r][c] == "B":
            br, bc = r, c
        elif board[r][c] == "R":
            rr, rc = r, c

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
visited = [[float("inf")] * (N * M) for _ in range(N * M)]
visited[rr * M + rc][br * M + bc] = 1
queue = deque([(rr, rc, br, bc, 0)])
flag = 0
while queue:
    rr, rc, br, bc, step = queue.popleft()
    for d in range(4):
        nrr, nrc, nbr, nbc = roll_red(rr, rc, br, bc, d)
        nbr, nbc = roll_blue(nrr, nrc, nbr, nbc, d)
        if nbr == -1 and nbc == -1:
            continue
        if nrr == -1 and nrc == -1:
            print(step + 1)
            flag = 1
            break
        else:
            # print(nrr, nrc, nbr, nbc)
            # print(len(visited))
            if visited[nrr * M + nrc][nbr * M + nbc] <= step + 1:
                continue
            else:
                visited[nrr * M + nrc][nbr * M + nbc] = step + 1
                queue.append((nrr, nrc, nbr, nbc, step + 1))
    if flag:
        break
else:
    print(-1)
