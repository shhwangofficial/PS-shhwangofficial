import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

board = [[0] * 101 for _ in range(101)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for r in range(x, x + 10):
        for c in range(y, y + 10):
            board[r][c] = 1

ans = 0
for row in board:
    ans += sum(row)

print(ans)
