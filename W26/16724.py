import sys

row, col = map(int, sys.stdin.readline().split())
board = []
for _ in range(row):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

visited = [[0] * col for _ in range(row)]
direct = {
    "D": [1, 0],
    "R": [0, 1],
    "U": [-1, 0],
    "L": [0, -1],
}
cycles = 0
sz = 0
for i in range(row):
    for j in range(col):
        if visited[i][j] == 0:
            cycles += 1
            visited[i][j] = cycles
            now_row = i
            now_col = j
            while True:
                cmd = direct[board[now_row][now_col]]
                next_row = now_row + cmd[0]
                next_col = now_col + cmd[1]
                if visited[next_row][next_col] == 0:
                    visited[next_row][next_col] = cycles
                    now_row = next_row
                    now_col = next_col
                elif visited[next_row][next_col] == cycles:
                    sz += 1
                    break
                else:
                    break

print(sz)
