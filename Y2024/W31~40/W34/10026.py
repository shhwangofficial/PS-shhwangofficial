import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0] * N for _ in range(N)]
area = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            area += 1
            stack = [(i, j)]
            color = board[i][j]
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    new_x, new_y = x + dx[k], y + dy[k]
                    if (
                        0 <= new_x < N
                        and 0 <= new_y < N
                        and visited[new_x][new_y] == 0
                        and board[new_x][new_y] == color
                    ):
                        visited[new_x][new_y] = 1
                        stack.append((new_x, new_y))
print(area, end=" ")

visited = [[0] * N for _ in range(N)]
area = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            area += 1
            stack = [(i, j)]
            color = board[i][j]
            if color == "R" or color == "G":
                color = ["R", "G"]
            else:
                color = ["B"]

            while stack:
                x, y = stack.pop()
                for k in range(4):
                    new_x, new_y = x + dx[k], y + dy[k]
                    if (
                        0 <= new_x < N
                        and 0 <= new_y < N
                        and visited[new_x][new_y] == 0
                        and board[new_x][new_y] in color
                    ):
                        visited[new_x][new_y] = 1
                        stack.append((new_x, new_y))
print(area, end=" ")
