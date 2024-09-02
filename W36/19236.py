import sys
import copy

fish_dict = {}
direction = [
    [],  # 0
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
]

board = [[0] * 4 for i in range(4)]

for i in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(0, 8, 2):
        fish_dict[line[j]] = [i, j // 2, line[j + 1]]
        board[i][j // 2] = line[j]

max_eaten = 0


def everything_moves(fish_dict, board, shark_r, shark_c, sum_eaten):
    _fish_dict = copy.deepcopy(fish_dict)
    _board = copy.deepcopy(board)

    eaten_fish = _board[shark_r][shark_c]
    _board[shark_r][shark_c] = 0
    sum_eaten += eaten_fish
    shark_direction = _fish_dict[eaten_fish][2]
    _fish_dict[eaten_fish] = 0

    for fish in range(1, 16 + 1):
        if _fish_dict[fish] == 0:
            continue
        r, c, d = _fish_dict[fish]
        for k in range(8):
            nr, nc, nd = r, c, d
            nd = (d + k - 1) % 8 + 1
            nr, nc = nr + direction[nd][0], nc + direction[nd][1]

            if 0 <= nr < 4 and 0 <= nc < 4 and not (nr == shark_r and nc == shark_c):
                switching_fish = _board[nr][nc]
                if switching_fish != 0:
                    _fish_dict[switching_fish] = [r, c, _fish_dict[switching_fish][2]]
                _fish_dict[fish] = [nr, nc, nd]
                _board[r][c], _board[nr][nc] = switching_fish, fish
                break

    flag = 1
    n_shark_r, n_shark_c = shark_r, shark_c
    while 1:
        n_shark_r += direction[shark_direction][0]
        n_shark_c += direction[shark_direction][1]

        if 0 <= n_shark_r < 4 and 0 <= n_shark_c < 4:
            if _board[n_shark_r][n_shark_c] == 0:
                continue
            flag = 0
            everything_moves(_fish_dict, _board, n_shark_r, n_shark_c, sum_eaten)
        else:
            break

    global max_eaten
    if flag and (max_eaten < sum_eaten):
        max_eaten = sum_eaten


everything_moves(fish_dict, board, 0, 0, 0)

print(max_eaten)
