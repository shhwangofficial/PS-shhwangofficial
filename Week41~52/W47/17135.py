import sys
from itertools import combinations
from collections import deque
import copy

N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = [0, -1, 0]
dc = [-1, 0, 1]

ans = 0
for comb in combinations(range(M), 3):
    board_copy = copy.deepcopy(board)
    temp = 0
    while board_copy:
        rows = len(board_copy)
        hit = [[0] * M for _ in range(rows)]
        hit_arr = []
        for archer in comb:
            visited = [[0] * M for _ in range(rows)]
            queue = deque([(rows - 1, archer, 0)])
            while queue:
                r, c, d = queue.popleft()
                if board_copy[r][c] == 1:
                    if not hit[r][c]:
                        hit[r][c] = 1
                        hit_arr.append((r, c))
                        temp += 1
                    break
                for i in range(3):
                    nr, nc, nd = r + dr[i], c + dc[i], d + 1
                    if nd <= D - 1 and 0 <= nr < rows and 0 <= nc < M and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc, nd))

        for hr, hc in hit_arr:
            board_copy[hr][hc] = 0

        board_copy.pop()

    ans = max(ans, temp)

print(ans)
