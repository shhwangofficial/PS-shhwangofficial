import sys

N, pE, pW, pS, pN = map(int, sys.stdin.readline().split())
p = [pE / 100, pW / 100, pS / 100, pN / 100]
dxdy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
board = [[0] * 30 for _ in range(30)]
board[15][15] = 1
sum_prob = 0


def doit(board, r, c, until_now_prob, round, last):
    if round == N:
        global sum_prob
        sum_prob += until_now_prob
        return
    _set = {0, 1, 2, 3} - {(last + 1) % 2 + 2 * (last // 2)}
    for i in _set:
        nr, nc = r + dxdy[i][0], c + dxdy[i][1]
        if board[nr][nc] == 1:
            pass
        else:
            board[nr][nc] = 1
            doit(board, nr, nc, until_now_prob * p[i], round + 1, i)
            board[nr][nc] = 0


doit(board, 15, 15, 1, 0, 99)
print(sum_prob)
