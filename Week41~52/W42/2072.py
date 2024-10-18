import sys

N = int(sys.stdin.readline())

board = [[0] * 19 for _ in range(19)]

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]


def check(r, c, bw):
    for d in range(4):
        left, right = 0, 0
        left_r, left_c = r, c
        right_r, right_c = r, c
        for i in range(5):
            nr, nc = left_r + dx[d], left_c + dy[d]
            if 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == bw:
                left += 1
                left_r, left_c = nr, nc
            else:
                break
        for i in range(5):
            nr, nc = right_r - dx[d], right_c - dy[d]
            if 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == bw:
                right += 1
                right_r, right_c = nr, nc
            else:
                break
        if left + right == 4:
            return True

    return False


for i in range(N):
    r, c = map(int, sys.stdin.readline().split())
    r -= 1
    c -= 1
    board[r][c] = i % 2 + 1
    if check(r, c, i % 2 + 1):
        print(i + 1)
        break
else:
    print(-1)
