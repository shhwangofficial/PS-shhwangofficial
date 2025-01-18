import sys

b_row, b_col = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(b_row)]
visited = [[0] * b_col for _ in range(b_row)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
area_no = 0
dic = {0: 0}
for i in range(b_row):
    for j in range(b_col):
        if board[i][j] == 1 and visited[i][j] == 0:
            area_no += 1
            visited[i][j] = area_no
            stack = [[i, j]]
            size = 0
            while stack:
                now_r, now_c = stack.pop()
                size += 1
                for k in range(4):
                    nr, nc = now_r + dx[k], now_c + dy[k]
                    if 0 <= nr < b_row and 0 <= nc < b_col and visited[nr][nc] == 0 and board[nr][nc] == 1:
                        visited[nr][nc] = area_no
                        stack.append([nr, nc])
            dic[area_no] = size

ans = 0
for i in range(b_row):
    for j in range(b_col):
        if board[i][j] == 0:
            set_ = set([])
            for k in range(4):
                nr, nc = i + dx[k], j + dy[k]
                if 0 <= nr < b_row and 0 <= nc < b_col:
                    set_.add(visited[nr][nc])

            temp = 1
            for area in list(set_):
                temp += dic[area]
            ans = max(temp, ans)

print(ans)
