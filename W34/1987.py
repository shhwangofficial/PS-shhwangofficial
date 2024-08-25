import sys

row, col = map(int, sys.stdin.readline().split())
board = []
for i in range(row):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

stack = [[0, 0, set(board[0][0])]]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
cnt = 1

while stack:
    now_x, now_y, now_set = stack.pop()
    for i in range(4):
        new_x = now_x + dx[i]
        new_y = now_y + dy[i]

        if 0 <= new_x < row and 0 <= new_y < col and board[new_x][new_y] not in now_set:
            new_set = set(now_set)
            new_set.add(board[new_x][new_y])
            if len(new_set) > cnt:
                cnt = len(new_set)
            stack.append([new_x, new_y, new_set])

print(cnt)
