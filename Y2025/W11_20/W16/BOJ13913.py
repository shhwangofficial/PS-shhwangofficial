import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, K = map(int, input().split())
visited = [0] * 200001
visited[N] = 1
path = [-1] * 200001
queue = deque([(N, 0)])
while queue:
    now, step = queue.popleft()
    if now == K:
        break
    for d in (-1, 1, now):
        new = now + d
        if 0 <= new < 200001 and visited[new] == 0:
            visited[new] = 1
            path[new] = now
            queue.append((new, step + 1))
print(step)
nxt = K
ans = []
while nxt != -1:
    ans.append(nxt)
    nxt = path[nxt]
ans.reverse()
print(*ans)
