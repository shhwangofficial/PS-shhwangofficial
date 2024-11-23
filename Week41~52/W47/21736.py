import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


ans = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == "I":
            stack = [(i, j)]
            visited[i][j] = 1
            while stack:
                r, c = stack.pop()
                if board[r][c] == "P":
                    ans += 1
                for i in range(4):
                    nr, nc = r + dx[i], c + dy[i]
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and board[nr][nc] != "X":
                        visited[nr][nc] = 1
                        stack.append((nr, nc))
            print(ans if ans > 0 else "TT")
            exit()
