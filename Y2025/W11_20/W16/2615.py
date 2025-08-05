import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

board = [list(map(int, input().split())) for _ in range(19)]
visited = [[[0] * 19 for _ in range(19)] for _ in range(4)]

dr = [1, 1, 0, -1]
dc = [0, 1, 1, 1]


def solve():
    for c in range(19):
        for r in range(19):
            if board[r][c]:
                stone = board[r][c]
                for d in range(4):
                    nr, nc = r, c
                    cnt = 0
                    while 0 <= nr < 19 and 0 <= nc < 19:
                        if not visited[d][nr][nc] and board[nr][nc] == stone:
                            visited[d][nr][nc] = 1
                            cnt += 1
                            nr, nc = nr + dr[d], nc + dc[d]
                        else:
                            break
                    if cnt == 5:
                        return stone, r, c
    return 0, -1, -1


res, rnum, cnum = solve()

print(res)
if res != 0:
    print(rnum + 1, cnum + 1)
