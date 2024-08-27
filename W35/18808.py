import sys

rows, cols, no_stickers = map(int, sys.stdin.readline().split())

board = [[0] * cols for _ in range(rows)]
for _ in range(no_stickers):
    row_now, col_now = map(int, sys.stdin.readline().split())
    sticker = []
    for i in range(row_now):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    for rot in range(4):
        if rot != 0:
            row_now = len(sticker)
            col_now = len(sticker[0])
            temp_sticker = [[0] * row_now for _ in range(col_now)]
            for i in range(row_now):
                for j in range(col_now):
                    temp_sticker[j][row_now - i - 1] = sticker[i][j]
            sticker = temp_sticker
            row_now = len(sticker)
            col_now = len(sticker[0])
        flag_sticker = 0
        for i in range(rows - row_now + 1):
            for j in range(cols - col_now + 1):
                for k in range(row_now):
                    flag = 0
                    for l in range(col_now):
                        if 0 <= k + i < rows and 0 <= l + j < cols:
                            if sticker[k][l] == 1 and board[k + i][l + j] == 1:
                                flag = 1
                                break
                        else:
                            flag = 1
                            break
                    if flag:
                        break
                else:
                    for k in range(row_now):
                        for l in range(col_now):
                            if sticker[k][l] == 1:
                                board[k + i][l + j] = 1
                    flag_sticker = 1
                    break
            if flag_sticker:
                break
        if flag_sticker:
            break

cnt = 0
for row in board:
    cnt += sum(row)

print(cnt)
