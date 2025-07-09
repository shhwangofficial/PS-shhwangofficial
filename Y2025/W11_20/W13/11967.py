import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N * N)]
visited = set()
turned = set()
for _ in range(M):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    graph[a * N + b].append(c * N + d)

from collections import deque

queue = deque([0])
visited.add(0)
turned.add(0)
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        turned.add(nxt)
        r, c = nxt // N, nxt % N
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and nr * N + nc in visited and r * N + c not in visited:
                visited.add(r * N + c)
                queue.append(r * N + c)
                break

    r, c = now // N, now % N
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and nr * N + nc not in visited and nr * N + nc in turned:
            visited.add(nr * N + nc)
            queue.append(nr * N + nc)
print(len(turned))
