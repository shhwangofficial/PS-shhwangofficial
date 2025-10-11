import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
W = int(input())
saguns = [(0, 0)] + [list(map(int, input().split())) for _ in range(W)]
dp = [[float("inf")] * (W + 1) for _ in range(W + 1)]
path = [[float("inf")] * (W + 1) for _ in range(W + 1)]
dp[0][0] = 0


def dist(i, j):
    return abs(saguns[j][0] - saguns[i][0]) + abs(saguns[j][1] - saguns[i][1])


def from_origin(i, origin):
    if origin == 2:
        origin = N
    return abs(origin - saguns[i][0]) + abs(origin - saguns[i][1])


for r in range(W):
    for c in range(W):
        now = max(r, c)
        if r == 0:
            if dp[now + 1][c] > dp[r][c] + from_origin(now + 1, 1):
                dp[now + 1][c] = dp[r][c] + from_origin(now + 1, 1)
                path[now + 1][c] = (1, r, c)
        else:
            if dp[now + 1][c] > dp[r][c] + dist(now + 1, r):
                dp[now + 1][c] = dp[r][c] + dist(now + 1, r)
                path[now + 1][c] = (1, r, c)
        if c == 0:
            if dp[r][now + 1] > dp[r][c] + from_origin(now + 1, 2):
                dp[r][now + 1] = dp[r][c] + from_origin(now + 1, 2)
                path[r][now + 1] = (2, r, c)
        else:
            if dp[r][now + 1] > dp[r][c] + dist(now + 1, c):
                dp[r][now + 1] = dp[r][c] + dist(now + 1, c)
                path[r][now + 1] = (2, r, c)


ans_path = []
ans, tmp = float("inf"), ()
for i in range(W):
    if ans > dp[i][W]:
        tmp = path[i][W]
        ans = dp[i][W]
    if ans > dp[W][i]:
        tmp = path[W][i]
        ans = dp[W][i]

while tmp != float("inf"):
    ans_path.append(tmp[0])
    tmp = path[tmp[1]][tmp[2]]

print(ans)
for i in range(W - 1, -1, -1):
    print(ans_path[i])
