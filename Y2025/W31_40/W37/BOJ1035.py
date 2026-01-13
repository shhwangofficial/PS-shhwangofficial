import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
from itertools import combinations, permutations

board = [input() for _ in range(5)]
stars = []
for r in range(5):
    for c in range(5):
        if board[r][c] == "*":
            stars.append(r * 5 + c)

no_stars = len(stars)
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

route = [[[float("inf")] * 5 for _ in range(5)] for i in range(no_stars)]
for i in range(no_stars):
    queue = deque([(0, stars[i])])
    route[i][stars[i] // 5][stars[i] % 5] = 0
    while queue:
        step, now = queue.popleft()
        r, c = now // 5, now % 5
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 5 and 0 <= nc < 5 and route[i][nr][nc] > step + 1:
                route[i][nr][nc] = step + 1
                queue.append((step + 1, nr * 5 + nc))

ans = float("inf")
for comb in combinations(range(25), no_stars):
    s = comb[0]
    set_ = set(comb)
    visited = [0] * 25
    visited[s] = 1
    stack = [s]
    while stack:
        now = stack.pop()
        r, c = now // 5, now % 5
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            nxt = nr * 5 + nc
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nxt] == 0 and nxt in set_:
                visited[nxt] = 1
                stack.append(nxt)
    err = 0
    for c in comb:
        if visited[c] == 0:
            err = 1
            break
    if err:
        continue

    for perm in permutations(range(no_stars), no_stars):
        temp = 0
        for i in range(no_stars):
            temp += route[perm[i]][comb[i] // 5][comb[i] % 5]

        ans = min(temp, ans)

print(ans)
