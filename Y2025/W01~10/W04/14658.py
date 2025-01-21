import sys

N, M, L, K = map(int, sys.stdin.readline().split())
stars = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

ans = 0
for s in range(K):
    for t in range(K):
        x, y = stars[s][0], stars[t][1]
        cnt = 0
        for star in stars:
            if x <= star[0] <= x + L and y <= star[1] <= y + L:
                cnt += 1
        ans = max(ans, cnt)

print(K - ans)
