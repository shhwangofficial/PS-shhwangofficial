import sys

T = int(sys.stdin.readline())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0] * N for i in range(M)]
    visited = [[0] * N for i in range(M)]
    for k in range(K):
        a, b = map(int, sys.stdin.readline().split())
        board[a][b] = 1
    ans = 0

    for i in range(M):
        for j in range(N):
            if board[i][j] == 1 and visited[i][j] == 0:
                ans += 1
                stack = [(i, j)]
                visited[i][j] = 1
                while stack:
                    r, c = stack.pop()
                    for d in range(4):
                        nr, nc = r + dx[d], c + dy[d]
                        if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == 1:
                            visited[nr][nc] = 1
                            stack.append((nr, nc))

    print(ans)
