import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
for size in range(min(N, M), 0, -1):
    d = size - 1
    for r in range(N):
        for c in range(M):
            if r + d < N and c + d < M:
                val = board[r][c]
                if val == board[r + d][c] and val == board[r][c + d] and val == board[r + d][c + d]:
                    print(size**2)
                    exit()
