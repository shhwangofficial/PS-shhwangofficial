import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
comm = list(map(int, input().split()))

dice = [[0, 0, 0] for _ in range(4)]


def up(dice):
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]


def down(dice):
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]


def right(dice):
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]


def left(dice):
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dc = [0, right, left, up, down]
for c in comm:
    nx, ny = x + dx[c], y + dy[c]
    if 0 <= nx < N and 0 <= ny < M:
        dc[c](dice)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[3][1]
        else:
            dice[3][1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[1][1])
        x, y = nx, ny
