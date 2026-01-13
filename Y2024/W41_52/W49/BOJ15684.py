import sys
from itertools import combinations

N, M, H = map(int, sys.stdin.readline().split())
edge_set = set()
for i in range(1, H + 1):
    for j in range(1, N):
        edge_set.add((i, j))
board = [[0] * (N + 1) for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    for k in (-1, 0, 1):
        edge_set.discard((a, b + k))

    board[a][b] = b + 1
    board[a][b + 1] = b


def play(board, ans):
    for s in range(1, N + 1):
        now = s
        level = 1
        while level <= H:
            if board[level][now]:
                now = board[level][now]
            level += 1
        if now != s:
            return

    print(ans)
    exit()


for k in range(0, 4):
    for comb in combinations(edge_set, k):
        for a, b in comb:
            board[a][b] = b + 1
            board[a][b + 1] = b
        play(board, k)
        for a, b in comb:
            board[a][b] = 0
            board[a][b + 1] = 0

print(-1)
