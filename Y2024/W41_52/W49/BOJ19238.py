import sys
from collections import deque, defaultdict

N, M, F = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

s_r, s_c = map(lambda x: int(x) - 1, sys.stdin.readline().split())

dic = defaultdict(int)
for _ in range(M):
    pr, pc, gr, gc = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    dic[pr * N + pc] = [gr, gc]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

queue = deque([(s_r, s_c, F)])
visited = [[0] * N for _ in range(N)]
visited[s_r][s_c] = 1

while queue:
    queue = deque(sorted(queue, key=lambda x: (-x[2], x[0], x[1])))
    r, c, f = queue.popleft()

    if dic[r * N + c]:
        goal = dic[r * N + c]
        queue_goal = deque([(r, c, f)])
        visited_goal = [[0] * N for _ in range(N)]
        visited_goal[r][c] = 1
        while queue_goal:
            gr, gc, gf = queue_goal.popleft()
            if [gr, gc] == goal:
                f = gf + (f - gf) * 2
                break
            if gf:
                for i in range(4):
                    ngr, ngc, ngf = gr + dx[i], gc + dy[i], gf - 1
                    if 0 <= ngr < N and 0 <= ngc < N and visited_goal[ngr][ngc] == 0 and board[ngr][ngc] == 0:
                        visited_goal[ngr][ngc] = 1
                        queue_goal.append((ngr, ngc, ngf))
        else:
            print(-1)
            exit()

        queue = deque([goal + [f]])
        visited = [[0] * N for _ in range(N)]
        visited[goal[0]][goal[1]] = 1
        dic[r * N + c] = 0

        for i in dic.keys():
            if dic[i] != 0:
                break
        else:
            print(f)
            exit()

        continue

    if f:
        for i in range(4):
            nr, nc, nf = r + dx[i], c + dy[i], f - 1
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr, nc, nf))

print(-1)
