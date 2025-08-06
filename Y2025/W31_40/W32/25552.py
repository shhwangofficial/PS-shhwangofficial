import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, M = map(int, input().split())

before = [input() for _ in range(N)]
D = int(input())
after = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue = deque([])

for r in range(N):
    for c in range(M):
        if before[r][c] == "O":
            queue.append((r, c))
            visited[r][c] = 1

mulr = [1, 1, -1, -1]
mulc = [-1, 1, 1, -1]
while queue:
    r, c = queue.popleft()
    for dr in range(0, D + 1):
        for dc in range(0, D - dr + 1):
            for i in range(4):
                nr, nc = r + dr * mulr[i], c + dc * mulc[i]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and after[nr][nc] == "O":
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

for r in range(N):
    for c in range(M):
        if after[r][c] == "O":
            if visited[r][c] == 0:
                print("NO")
                exit()
        elif after[r][c] == "X":
            if before[r][c] == "O":
                print("NO")
                exit()
print("YES")
