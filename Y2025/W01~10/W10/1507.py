import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]
for k in range(N):
    for a in range(N):
        for b in range(N):
            if a != k and b != k:
                if board[a][k] + board[k][b] < board[a][b]:
                    print(-1)
                    exit()
                elif board[a][k] + board[k][b] == board[a][b]:
                    check[a][b] = 1
                    check[b][a] = 1

ans = 0
for r in range(N):
    for c in range(r + 1, N):
        if check[r][c] != 1:
            ans += board[r][c]
print(ans)
