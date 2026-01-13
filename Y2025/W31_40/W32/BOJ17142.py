import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
inactive = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            inactive.append(r * N + c)


def backtrack(lst, idx):
    if len(lst) == M:
        ans = bfs(lst)
        return ans
    ans = float("inf")
    for i in range(idx + 1, len(inactive)):
        ans = min(ans, backtrack(lst + [inactive[i]], i))

    return ans


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(lst):
    queue = deque([])
    visited = [[float("inf")] * N for _ in range(N)]
    for i in lst:
        r, c = i // N, i % N
        queue.append((0, r, c))
        visited[r][c] = 0
    while queue:
        stp, r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > stp + 1 and board[nr][nc] != 1:
                visited[nr][nc] = stp + 1
                queue.append((stp + 1, nr, nc))
    ans = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] == float("inf") and board[r][c] == 0:
                return float("inf")
            if board[r][c] == 0:
                ans = max(ans, visited[r][c])
    return ans


ans = backtrack([], -1)
if ans == float("inf"):
    print(-1)
else:
    print(ans)
