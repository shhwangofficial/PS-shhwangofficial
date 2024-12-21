import sys
from collections import defaultdict

N, M, K = map(int, sys.stdin.readline().split())

board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]

total = 0
for r in range(K):
    for c in range(K):
        dic = defaultdict(int)

        for rs in range(N // K):
            for cs in range(M // K):
                dic[board[r + rs * K][c + cs * K]] += 1

        max_ = 0
        for key in dic:
            if dic[key] > max_:
                temp = key
                max_ = dic[key]

        for rs in range(N // K):
            for cs in range(M // K):
                if board[r + rs * K][c + cs * K] != temp:
                    total += 1
                    board[r + rs * K][c + cs * K] = temp

print(total)
for row in board:
    print("".join(row))
