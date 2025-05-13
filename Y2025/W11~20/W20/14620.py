import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
sum_board = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for r in range(1, N - 1):
    for c in range(1, N - 1):
        sum_board[r][c] = board[r][c]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            sum_board[r][c] += board[nr][nc]

ans = float("inf")


def backtrack(n, temp):
    global ans
    if temp > ans:
        return
    if n == 3:
        ans = min(ans, temp)
        return

    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if not visited[r][c]:
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if visited[nr][nc]:
                        break
                else:
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        visited[nr][nc] = 1
                    visited[r][c] = 1
                    backtrack(n + 1, temp + sum_board[r][c])
                    visited[r][c] = 0
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        visited[nr][nc] = 0


backtrack(0, 0)
print(ans)
