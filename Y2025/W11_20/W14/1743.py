import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

max_food = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 1 and visited[r][c] == 0:
            visited[r][c] = 1
            stack = [(r, c)]
            temp_size = 0
            while stack:
                R, C = stack.pop()
                temp_size += 1
                for d in range(4):
                    nR, nC = R + dr[d], C + dc[d]
                    if 0 <= nR < N and 0 <= nC < M:
                        if board[nR][nC] == 1 and visited[nR][nC] == 0:
                            visited[nR][nC] = 1
                            stack.append((nR, nC))

            max_food = max(max_food, temp_size)

print(max_food)
