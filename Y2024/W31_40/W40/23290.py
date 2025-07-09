import sys

M, S = map(int, sys.stdin.readline().split())

board_smell = [[0] * 4 for _ in range(4)]
fish_list = []
for _ in range(M):
    r, c, d = map(lambda x: (int(x) - 1) % 8, sys.stdin.readline().split())
    fish_list.append([r, c, d])

shark_r, shark_c = map(lambda x: int(x) - 1, sys.stdin.readline().split())

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
shark_d = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def move_shark(s_r, s_c, depth, eaten, visited):
    if depth == 3:
        global max_eaten
        if eaten > max_eaten:
            global shark_r, shark_c, path
            shark_r, shark_c, path, max_eaten = s_r, s_c, visited, eaten
        return

    for i in range(4):
        n_shark_r, n_shark_c = s_r + shark_d[i][0], s_c + shark_d[i][1]
        if 0 <= n_shark_r < 4 and 0 <= n_shark_c < 4:
            idx = n_shark_r * 4 + n_shark_c
            if visited & (1 << idx):
                move_shark(n_shark_r, n_shark_c, depth + 1, eaten, visited)
            else:
                move_shark(
                    n_shark_r, n_shark_c, depth + 1, eaten + len(board_fish[n_shark_r][n_shark_c]), visited | (1 << idx)
                )


for _ in range(S):
    board_fish = [[[] for i in range(4)] for _ in range(4)]
    for fish in fish_list:
        r, c, d = fish
        for i in range(8):
            nd = (d - i) % 8
            nr, nc = r + dx[nd], c + dy[nd]
            if 0 <= nr < 4 and 0 <= nc < 4 and board_smell[nr][nc] == 0 and (nr != shark_r or nc != shark_c):
                board_fish[nr][nc].append(nd)
                break
        else:
            board_fish[r][c].append(d)

    max_eaten = -1
    path = 0

    move_shark(shark_r, shark_c, 0, 0, 0)

    for i in range(16):
        if path & (1 << i):
            eaten_r, eaten_c = i // 4, i % 4
            if board_fish[eaten_r][eaten_c]:
                board_smell[eaten_r][eaten_c] = 3
            board_fish[eaten_r][eaten_c] = []

    for fish in fish_list:
        r, c, d = fish
        board_fish[r][c].append(d)

    fish_list = []
    for i in range(4):
        for j in range(4):
            if len(board_fish[i][j]) > 0:
                for fish_d in board_fish[i][j]:
                    fish_list.append([i, j, fish_d])
            if board_smell[i][j] > 0:
                board_smell[i][j] -= 1

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(board_fish[i][j])
print(ans)
