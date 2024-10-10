import sys
from collections import deque

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
left = min(board[0][0], board[N - 1][N - 1])
ans = 201
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while left >= 0:
    right_s = max(board[0][0], board[N - 1][N - 1])
    right_e = 200
    temp = 0
    while right_s <= right_e:
        mid = (right_s + right_e) // 2
        visited = [[0] * N for _ in range(N)]
        queue = deque([[0, 0]])
        visited[0][0] = 1
        while queue:
            r, c = queue.popleft()
            if r == N - 1 and c == N - 1:
                temp = mid
                right_e = mid - 1
                break
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and left <= board[nr][nc] <= mid:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
        else:
            right_s = mid + 1
    if temp:
        ans = min(ans, temp - left)
    left -= 1

print(ans)
