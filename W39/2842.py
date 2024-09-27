import sys
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(str, sys.stdin.readline().rstrip())) for i in range(N)]
abs_levels = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
inf = 10**8

num_houses = 0
heights = set({})
min_house_height = inf
max_house_height = 0
max_height = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == "P":
            s_r, s_c = i, j
            min_house_height = min(min_house_height, abs_levels[i][j])
            max_house_height = max(max_house_height, abs_levels[i][j])
        elif board[i][j] == "K":
            num_houses += 1
            min_house_height = min(min_house_height, abs_levels[i][j])
            max_house_height = max(max_house_height, abs_levels[i][j])
        heights.add(abs_levels[i][j])
        max_height = max(max_height, abs_levels[i][j])

heights = sorted(list(heights))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(low, high, num_houses):
    queue = deque([[s_r, s_c]])
    visited = [[0] * (N) for _ in range(N)]
    visited[s_r][s_c] = 1
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and low <= abs_levels[nr][nc] <= high:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
                    if board[nr][nc] == "K":
                        num_houses -= 1
    return not num_houses


ans = inf
for height in heights:
    if height > min_house_height:
        break
    s, e = max_house_height, max_height
    temp = inf
    while s <= e:
        mid = (s + e) // 2
        if BFS(height, mid, num_houses):
            temp = mid
            e = mid - 1
        else:
            s = mid + 1

    if temp == inf:
        continue
    else:
        ans = min(ans, temp - height)
print(ans)
