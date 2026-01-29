import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]


def move(r, c, d, s):
    return (r + s * dr[d]) % N, (c + s * dc[d]) % N


clouds = set([(N - 1) * N, (N - 1) * N + 1, (N - 2) * N, (N - 2) * N + 1])
for _ in range(M):
    d, s = map(int, input().split())
    new_clouds = set([])
    for cloud in clouds:
        nr, nc = move(cloud // N, cloud % N, d - 1, s)
        board[nr][nc] += 1
        new_clouds.add(nr * N + nc)

    for new_cloud in new_clouds:
        r, c = new_cloud // N, new_cloud % N
        for d in range(1, 8, 2):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
                board[r][c] += 1
    clouds = set([])
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and r * N + c not in new_clouds:
                clouds.add(r * N + c)
                board[r][c] -= 2

print(sum(map(sum, board)))
