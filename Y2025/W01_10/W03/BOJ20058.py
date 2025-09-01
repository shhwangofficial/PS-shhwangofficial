from collections import deque

N, Q = map(int, input().split())

board = []
for i in range(2**N):
    board.append(list(map(int, input().split())))

query = map(int, input().split())


def rotation(std_r, std_c, size):
    temp = []
    for local_r in range(size):
        for local_c in range(size):
            temp.append((std_r + local_c, std_c + (size - local_r - 1), board[std_r + local_r][std_c + local_c]))

    for r, c, val in temp:
        board[r][c] = val


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in query:
    for r in range(0, 2**N, 2**i):
        for c in range(0, 2**N, 2**i):
            rotation(r, c, 2**i)

    temp = []
    for r in range(2**N):
        for c in range(2**N):
            stack = 0
            for d in range(4):
                nr, nc = r + dx[d], c + dy[d]
                if 0 <= nr < 2**N and 0 <= nc < 2 ** N and board[nr][nc] > 0:
                    stack += 1
            if stack < 3:
                temp.append((r, c))

    for r, c in temp:
        board[r][c] = max(board[r][c] - 1, 0)


sum_ = 0
for line in board:
    sum_ += sum(line)

print(sum_)

max_ = 0
visited = [[0] * 2**N for i in range(2**N)]

for r in range(2**N):
    for c in range(2**N):
        if visited[r][c] == 0 and board[r][c] > 0:
            visited[r][c] = 1
            score = 0
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                score += 1
                max_ = max(max_, score)
                for d in range(4):
                    nr, nc = row + dx[d], col + dy[d]
                    if (0 <= nr < 2**N and 0 <= nc < 2**N) and visited[nr][nc] == 0 and board[nr][nc] > 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
print(max_)
