import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
to = [list(map(int, input())) for _ in range(N)]

cnt = 0
for r in range(N - 3 + 1):
    for c in range(M - 3 + 1):
        if board[r][c] != to[r][c]:
            cnt += 1
            for R in range(r, r + 3):
                for C in range(c, c + 3):
                    board[R][C] = (board[R][C] + 1) % 2

for r in range(N):
    for c in range(M):
        if board[r][c] != to[r][c]:
            print(-1)
            exit()

print(cnt)
