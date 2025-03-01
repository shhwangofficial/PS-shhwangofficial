M, N = map(int, input().split())
board = [list(map(int, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(row, col):
    stack = []

    while True:
        if row == M - 1:
            return True

        if visited[row][col] == 0:
            visited[row][col] = 1

        for d in range(4):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < M and 0 <= ncol < N and board[nrow][ncol] == 0:
                if visited[nrow][ncol] == 0:
                    stack.append([nrow, ncol])
                    row, col = nrow, ncol
                    break
        else:
            if stack:
                row, col = stack.pop()
            else:
                return False


for col in range(N):
    if board[0][col] == 0:
        if dfs(0, col):
            print("YES")
            break

else:
    print("NO")
