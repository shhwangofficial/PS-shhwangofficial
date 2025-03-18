import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N = int(input())
board = [list(map(str, input())) for _ in range(N)]
B, E = [], []
for r in range(N):
    for c in range(N):
        if board[r][c] == "B":
            B.append((r, c))
        elif board[r][c] == "E":
            E.append((r, c))
if B[0][0] == B[1][0]:
    Bstate = 0  # 가로
else:
    Bstate = 1  # 세로
if E[0][0] == E[1][0]:
    Estate = 0  # 가로
else:
    Estate = 1  # 세로
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

sr, sc, gr, gc = B[1][0], B[1][1], E[1][0], E[1][1]
queue = deque([(sr, sc, Bstate, 0)])
visited = [[[0] * N for _ in range(N)] for _ in range(2)]
visited[Bstate][sr][sc] = 1
while queue:
    r, c, state, step = queue.popleft()
    if r == gr and c == gc and state == Estate:
        print(step)
        break
    if state == 0:
        lst = [(r, c), (r, c - 1), (r, c + 1)]
    else:
        lst = [(r, c), (r - 1, c), (r + 1, c)]

    for d in range(4):
        for s in range(3):
            nr, nc = lst[s][0] + dr[d], lst[s][1] + dc[d]
            if not (0 <= nr < N and 0 <= nc < N and board[nr][nc] != "1"):
                break
            else:
                if s == 0 and visited[state][nr][nc] != 0:
                    break
        else:
            nr, nc = lst[0][0] + dr[d], lst[0][1] + dc[d]
            visited[state][nr][nc] = step + 1
            queue.append((nr, nc, state, step + 1))
    flag = 0
    for ar in range(r - 1, r + 1 + 1):
        for ac in range(c - 1, c + 1 + 1):
            if not (0 <= ar < N and 0 <= ac < N and board[ar][ac] != "1"):
                flag = 1
                break
        if flag:
            break
    else:
        if visited[(state + 1) % 2][r][c] == 0:
            visited[(state + 1) % 2][r][c] = step + 1
            queue.append((r, c, (state + 1) % 2, step + 1))


else:
    print(0)
