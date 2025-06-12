import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
ans = 0
while True:
    groups = dict()
    visited = [[0] * N for _ in range(N)]
    i = 0
    continued = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                queue = deque([(r, c)])
                i += 1
                groups[i] = [(r, c, board[r][c])]
                visited[r][c] = 1
                while queue:
                    nowr, nowc = queue.popleft()
                    for j in range(4):
                        nxtr, nxtc = nowr + dr[j], nowc + dc[j]
                        if 0 <= nxtr < N and 0 <= nxtc < N:
                            if not visited[nxtr][nxtc] and L <= abs(board[nowr][nowc] - board[nxtr][nxtc]) <= R:
                                continued = 1
                                visited[nxtr][nxtc] = 1
                                queue.append((nxtr, nxtc))
                                groups[i].append((nxtr, nxtc, board[nxtr][nxtc]))

    if not continued:
        break

    for key in groups.keys():
        temp = 0
        for r, c, val in groups[key]:
            temp += val
        for r, c, val in groups[key]:
            board[r][c] = int(temp / len(groups[key]))

    ans += 1

print(ans)
