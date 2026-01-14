import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
trees = []
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    trees.append([z, x, y])
trees.sort()
trees = deque(trees)
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
year = 1
while year <= K:
    # spring
    new_trees = deque()
    dead_trees = deque()
    while trees:
        z, x, y = trees.popleft()
        if z > board[x][y]:
            dead_trees.append([z, x, y])
        else:
            board[x][y] -= z
            new_trees.append([z + 1, x, y])
            if (z + 1) % 5 == 0:
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        new_trees.appendleft([1, nx, ny])
    # summer
    while dead_trees:
        z, x, y = dead_trees.popleft()
        board[x][y] += z // 2

    # winter
    for x in range(N):
        for y in range(N):
            board[x][y] += A[x][y]
    trees = new_trees

    year += 1

print(len(trees))
