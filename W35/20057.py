import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r, c = N // 2, N // 2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
multiple = 0
direct = -1
total_out = 0
while 1:
    multiple += 1
    flag = 0
    for i in range(2):  # 회전
        direct = (direct + 1) % 4
        if flag:
            break
        for j in range(multiple):  # 나아가기
            if flag:
                break
            direct_x, direct_y = dx[direct], dy[direct]
            r += direct_x
            c += direct_y
            if r == 0 and c == 0:
                flag = 1
            sand_total = board[r][c]
            board[r][c] = 0
            remain_sand = sand_total
            if direct_x == 0:
                for ddx, ddy, percent in [
                    [0, (2 * direct_y), 0.05],
                    [1, direct_y, 0.1],
                    [-1, direct_y, 0.1],
                    [2, 0, 0.02],
                    [-2, 0, 0.02],
                    [-1, 0, 0.07],
                    [1, 0, 0.07],
                    [1, (-direct_y), 0.01],
                    [-1, (-direct_y), 0.01],
                ]:
                    temp_r, temp_c = r + ddx, c + ddy
                    blown_sand = int(sand_total * percent)
                    if 0 <= temp_r < N and 0 <= temp_c < N:
                        board[temp_r][temp_c] += blown_sand
                    else:
                        total_out += blown_sand
                    remain_sand -= blown_sand

            elif direct_y == 0:
                for ddx, ddy, percent in [
                    [(2 * direct_x), 0, 0.05],
                    [direct_x, 1, 0.1],
                    [direct_x, -1, 0.1],
                    [0, 2, 0.02],
                    [0, -2, 0.02],
                    [0, -1, 0.07],
                    [0, 1, 0.07],
                    [(-direct_x), 1, 0.01],
                    [(-direct_x), -1, 0.01],
                ]:
                    temp_r, temp_c = r + ddx, c + ddy
                    blown_sand = int(sand_total * percent)
                    if 0 <= temp_r < N and 0 <= temp_c < N:
                        board[temp_r][temp_c] += blown_sand
                    else:
                        total_out += blown_sand
                    remain_sand -= blown_sand

            temp_r, temp_c = r + direct_x, c + direct_y
            if 0 <= temp_r < N and 0 <= temp_c < N:
                board[temp_r][temp_c] += remain_sand
            else:
                total_out += remain_sand

    if flag == 1:
        break

print(total_out)
