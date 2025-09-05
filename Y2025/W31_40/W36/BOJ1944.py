import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
import heapq

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dic = dict()
i = 1
for r in range(1, N - 1):
    for c in range(1, N - 1):
        if board[r][c] == "S":
            sr, sc = r, c
            dic[0] = r * N + c
        elif board[r][c] == "K":
            dic[i] = r * N + c
            i += 1

visited = [[[float("inf")] * N for _ in range(N)] for i in range(M + 1)]
for i in range(M + 1):
    r, c = dic[i] // N, dic[i] % N
    visited[i][r][c] = 0
    queue = deque([(0, r, c)])
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    while queue:
        step, r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "1" and visited[i][nr][nc] > step + 1:
                visited[i][nr][nc] = step + 1
                queue.append((step + 1, nr, nc))

connected = [0] * (M + 1)
heap = [(0, 0)]
ans = 0
while heap:
    dis, now = heapq.heappop(heap)
    if connected[now]:
        continue
    connected[now] = 1
    ans += dis
    for i in range(1, M + 1):
        r, c = dic[i] // N, dic[i] % N
        heapq.heappush(heap, (visited[now][r][c], i))


print(-1 if ans == float("inf") else ans)
