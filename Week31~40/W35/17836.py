import sys
from collections import deque

rows, cols, time_limit = map(int, sys.stdin.readline().split())
board = []
for _ in range(rows):
    board.append(list(map(int, sys.stdin.readline().split())))

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
visited = [[0] * cols for i in range(rows)]
visited_w_gram = [[0] * cols for i in range(rows)]

queue = deque([[0, 0, 0, 0]])  # r,c,gram,time
while queue:
    r, c, gram, time = queue.pop()
    if r == rows - 1 and c == cols - 1:
        continue
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        ngram = gram
        if 0 <= nr < rows and 0 <= nc < cols:
            if board[nr][nc] == 2 or gram:
                ngram = 1
                if visited_w_gram[nr][nc] == 0 or visited_w_gram[nr][nc] > time + 1:
                    visited_w_gram[nr][nc] = time + 1
                    queue.append([nr, nc, ngram, visited_w_gram[nr][nc]])
            else:
                if board[nr][nc] == 1:
                    continue

                if visited[nr][nc] == 0 or visited[nr][nc] > time + 1:
                    visited[nr][nc] = time + 1
                    queue.append([nr, nc, ngram, visited[nr][nc]])

if (visited[rows - 1][cols - 1] == 0 or visited[rows - 1][cols - 1] > time_limit) and (
    visited_w_gram[rows - 1][cols - 1] == 0 or visited_w_gram[rows - 1][cols - 1] > time_limit
):
    print("Fail")
else:
    if visited[rows - 1][cols - 1] != 0:
        print(min(visited[rows - 1][cols - 1], visited_w_gram[rows - 1][cols - 1]))
    else:
        print(visited_w_gram[rows - 1][cols - 1])
