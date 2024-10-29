import sys

N, M, K = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direction_now = [0] + list(map(int, sys.stdin.readline().split()))
smell = [[0] * N for _ in range(N)]

d = {}
for i in range(M):
    priority = [0]
    for _ in range(4):
        priority.append(list(map(int, sys.stdin.readline().split())))
    d[i + 1] = priority

for r in range(N):
    for c in range(N):
        if board[r][c] > 0:
            smell[r][c] = [board[r][c], K]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

sharks = set([i for i in range(1, M + 1)])
time = 0
while len(list(sharks)) >= 2:
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                shark_no = board[r][c]
                for nd in d[shark_no][direction_now[shark_no]]:
                    nr, nc = r + dx[nd], c + dy[nd]
                    if 0 <= nr < N and 0 <= nc < N and smell[nr][nc] == 0:
                        if new_board[nr][nc] != 0:
                            if new_board[nr][nc] > shark_no:
                                sharks.discard(new_board[nr][nc])
                                new_board[nr][nc] = shark_no
                                direction_now[shark_no] = nd
                            else:
                                sharks.discard(shark_no)
                        else:
                            new_board[nr][nc] = shark_no
                            direction_now[shark_no] = nd
                        break
                else:
                    for nd in d[shark_no][direction_now[shark_no]]:
                        nr, nc = r + dx[nd], c + dy[nd]
                        if 0 <= nr < N and 0 <= nc < N and smell[nr][nc][0] == shark_no:
                            new_board[nr][nc] = shark_no
                            direction_now[shark_no] = nd
                            break

    for r in range(N):
        for c in range(N):
            if new_board[r][c] > 0:
                smell[r][c] = [new_board[r][c], K + 1]

    for r in range(N):
        for c in range(N):
            if smell[r][c] != 0:
                if smell[r][c][1] == 1:
                    smell[r][c] = 0
                else:
                    smell[r][c][1] -= 1

    board = new_board

    time += 1
    if time >= 1001:
        print(-1)
        break
else:
    print(time)
