import sys
from itertools import combinations
from collections import deque

N, M, G, R = map(int, sys.stdin.readline().split())

board = []
possible = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if row[j] == 2:
            possible.append(i * M + j)
    board.append(row)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solve(greens, reds):
    ret = 0
    visited = [[0] * M for _ in range(N)]
    queue_red = deque(list(map(lambda x: (x // M, x % M), reds)))
    queue_green = deque(list(map(lambda x: (x // M, x % M), greens)))
    for red_r, red_c in queue_red:
        visited[red_r][red_c] = 1
    for green_r, green_c in queue_green:
        visited[green_r][green_c] = 2

    while queue_red or queue_green:
        temp_red = set([])
        while queue_red:
            r, c = queue_red.popleft()
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 0 and visited[nr][nc] == 0:
                    temp_red.add(nr * M + nc)

        temp_green = set([])
        while queue_green:
            r, c = queue_green.popleft()
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 0 and visited[nr][nc] == 0:
                    if nr * M + nc in temp_red:
                        ret += 1
                        temp_red.remove(nr * M + nc)
                    else:
                        temp_green.add((nr * M + nc))
                    visited[nr][nc] = 2

        for remain in temp_red:
            queue_red.append((remain // M, remain % M))
            visited[remain // M][remain % M] = 1
        for remain in temp_green:
            queue_green.append((remain // M, remain % M))

    return ret


ans = 0

for selected in combinations(possible, G + R):
    for greens in combinations(selected, G):
        greens = set(greens)
        reds = set(selected) - greens
        temp = solve(greens, reds)

        ans = max(ans, temp)

print(ans)
