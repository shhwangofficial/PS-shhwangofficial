import sys

N, M, T = map(int, sys.stdin.readline().split())
board = [[0] * M]
sum_ = 0
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    board.append(lst)
    sum_ += sum(lst)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):
    deleted = 0
    x, d, k = map(int, sys.stdin.readline().split())
    for row in range(x, N + 1, x):
        temp = [0] * M
        if d == 0:
            for i in range(M):
                temp[(i + k) % M] = board[row][i]
        else:
            for i in range(M):
                temp[(i - k) % M] = board[row][i]
        board[row] = temp

    visited = [[0] * M for j in range(N + 1)]
    global_flag = 0
    for r in range(1, N + 1):
        for c in range(M):
            if visited[r][c] == 0 and board[r][c] > 0:
                visited[r][c] = 1
                val = board[r][c]
                queue = [[r, c]]
                local_flag = 0
                while queue:
                    tr, tc = queue.pop()
                    for k in range(4):
                        nr, nc = tr + dx[k], (tc + dy[k]) % M
                        if 0 < nr <= N and board[nr][nc] == val and visited[nr][nc] == 0:
                            local_flag = 1
                            visited[nr][nc] = 1
                            deleted += val
                            board[nr][nc] = 0
                            queue.append([nr, nc])
                if local_flag:
                    board[r][c] = 0
                    deleted += val
                    global_flag = 1

    if global_flag:
        sum_ -= deleted
    else:
        temp_sum = 0
        temp_cnt = 0
        for i in range(1, N + 1):
            for j in range(M):
                if board[i][j] > 0:
                    temp_cnt += 1
                    temp_sum += board[i][j]
        if temp_cnt == 0:
            continue
        avg = temp_sum / temp_cnt
        for i in range(1, N + 1):
            for j in range(M):
                if board[i][j] == 0:
                    continue
                elif board[i][j] > avg:
                    board[i][j] -= 1
                    sum_ -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1
                    sum_ += 1

print(sum_)
