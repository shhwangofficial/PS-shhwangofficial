from collections import deque

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = [[[] for i in range(C)] for _ in range(R)]
for _ in range(W):
    r, c, type = map(int, input().split())
    r, c = r - 1, c - 1
    walls[r][c].append(type)
temperature = [[0] * C for _ in range(R)]
watch_list = []
heaters = []
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
for r in range(R):
    for c in range(C):
        if board[r][c] == 5:
            watch_list.append((r, c))
        elif board[r][c] != 0:
            heaters.append((r, c, board[r][c]))


def check_wall(r, c, nr, nc):
    if r < nr:
        if 0 in walls[nr][c]:
            return False
        else:
            return True
    elif r > nr:
        if 0 in walls[r][c]:
            return False
        else:
            return True
    elif c < nc:
        if 1 in walls[r][c]:
            return False
        else:
            return True
    elif c > nc:
        if 1 in walls[r][nc]:
            return False
        else:
            return True


def spread(heater):
    r, c, d = heater
    r, c = r + dr[d], c + dc[d]
    if not (0 <= r < R and 0 <= c < C):
        return

    visited = [[[0] * C for _ in range(R)] for _ in range(2)]
    if d == 1 or d == 2:
        sub_d = (3, 4)
    else:
        sub_d = (1, 2)

    s = 5
    queue = deque([(r, c, s, 1)])
    while queue:
        r, c, s, truth = queue.popleft()
        if s == 0:
            continue
        if truth:
            temperature[r][c] += s
            for sd in sub_d:
                nr, nc = r + dr[sd], c + dc[sd]
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and visited[0][nr][nc] == 0
                    and visited[1][nr][nc] == 0
                    and check_wall(r, c, nr, nc)
                ):
                    visited[0][nr][nc] = 1
                    queue.append((nr, nc, s, 0))
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and visited[1][nr][nc] == 0 and check_wall(r, c, nr, nc):
            visited[1][nr][nc] = 1
            queue.append((nr, nc, s - 1, 1))


def share(r, c):
    for d in range(1, 5):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and temperature[nr][nc] < temperature[r][c] and check_wall(r, c, nr, nc):
            new_temperature[nr][nc] += (temperature[r][c] - temperature[nr][nc]) // 4
            new_temperature[r][c] -= (temperature[r][c] - temperature[nr][nc]) // 4


chocolate = 0
while True:
    for heater in heaters:
        spread(heater)
    new_temperature = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if temperature[r][c]:
                share(r, c)

    for r in range(R):
        for c in range(C):
            temperature[r][c] += new_temperature[r][c]

    for r in range(R):
        for c in range(C):
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                temperature[r][c] = max(0, temperature[r][c] - 1)

    chocolate += 1
    if chocolate > 100:
        break
    for r, c in watch_list:
        if temperature[r][c] < K:
            break
    else:
        break

print(chocolate)
