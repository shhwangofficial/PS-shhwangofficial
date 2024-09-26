import sys
from collections import deque

N, K, R = map(int, sys.stdin.readline().split())
land_group = [-1] * (N * N)
road = [set({}) for _ in range(N * N)]
for _ in range(R):
    r1, c1, r2, c2 = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    road[r1 * N + c1].add(r2 * N + c2)
    road[r2 * N + c2].add(r1 * N + c1)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(N * N):
    if land_group[i] == -1:
        queue = deque([i])
        land_group[i] = i
        while queue:
            now = queue.popleft()
            r, c = now // N, now % N
            for k in range(4):
                nr, nc = r + dx[k], c + dy[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if nr * N + nc not in road[now] and land_group[nr * N + nc] == -1:
                        land_group[nr * N + nc] = i
                        queue.append(nr * N + nc)
print(land_group)
ans = 0
cows = []
for cow in range(K):
    r1, c1 = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    cows.append(r1 * N + c1)

for i in range(K):
    for j in range(i + 1, K):
        if land_group[cows[i]] != land_group[cows[j]]:
            ans += 1

print(ans)
