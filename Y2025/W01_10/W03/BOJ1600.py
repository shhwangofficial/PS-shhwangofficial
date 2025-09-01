import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
visited = [[[0] * W for _ in range(H)] for i in range(K + 1)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
hr = [-2, -1, 1, 2, 2, 1, -1, -2]
hc = [1, 2, 2, 1, -1, -2, -2, -1]

queue = deque([(0, 0, 0, 0)])  # r, c, step, horse
while queue:
    r, c, step, horse = queue.popleft()
    if r == H - 1 and c == W - 1:
        print(step)
        exit()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < H and 0 <= nc < W and visited[horse][nr][nc] == 0 and board[nr][nc] == 0:
            visited[horse][nr][nc] = 1
            queue.append((nr, nc, step + 1, horse))
    if horse < K:
        for i in range(8):
            nr, nc = r + hr[i], c + hc[i]
            if 0 <= nr < H and 0 <= nc < W and visited[horse + 1][nr][nc] == 0 and board[nr][nc] == 0:
                visited[horse + 1][nr][nc] = 1
                queue.append((nr, nc, step + 1, horse + 1))
print(-1)
