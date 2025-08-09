import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def dfs(now, lev, vis):
    if lev == 4:
        print(1)
        exit()
    for nxt in graph[now]:
        if not (1 << nxt & vis):
            dfs(nxt, lev + 1, vis | (1 << nxt))


for i in range(N):
    dfs(i, 0, 1 << i)
print(0)
