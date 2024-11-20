import sys
import copy

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cameras = []
total = N * M
for r in range(N):
    for c in range(M):
        if 0 < board[r][c] <= 6:
            if board[r][c] < 6:
                cameras.append((r, c, board[r][c]))
            else:
                total -= 1

d = {
    1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]],
}


def backtrack(camera, visited):
    if camera >= len(cameras):
        ret = 0
        for r in range(N):
            for c in range(M):
                if visited[r][c]:
                    ret += 1
        return ret
    
    temp = 0
    for i in d[cameras[camera][2]]:
        temp_visited = copy.deepcopy(visited)
        for dx, dy in i:
            stack = [(cameras[camera][0], cameras[camera][1])]
            temp_visited[cameras[camera][0]][cameras[camera][1]] = 1
            while stack:
                r, c = stack.pop()
                nr, nc = r + dx, c + dy
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 6:
                    temp_visited[nr][nc] = 1
                    stack.append((nr, nc))

        temp = max(backtrack(camera + 1, temp_visited), temp)

    return temp


visited = [[0] * M for _ in range(N)]
print(total - backtrack(0, visited))
