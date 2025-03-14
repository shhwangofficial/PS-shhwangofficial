import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, A, B, M = map(int, input().split())
edges = []
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    edges.append((s, e, cost))
    graph[s].append(e)


money = list(map(int, input().split()))
dist = [float("-inf")] * N
dist[A] = money[A]
flag = 0
cycler = set([])
for i in range(N):
    for s, e, cost in edges:
        if dist[s] != float("-inf") and dist[s] - cost + money[e] > dist[e]:
            if i == N - 1:
                cycler.add(s)
            else:
                dist[e] = dist[s] - cost + money[e]


def dfs(now):
    for nxt in graph[now]:
        if nxt == B:
            print("Gee")
            exit()
        if nxt not in visited:
            visited.add(nxt)
            dfs(nxt)


if dist[B] == float("-inf"):
    print("gg")

else:
    if A in cycler:
        print("Gee")
    else:
        for cyc in cycler:
            visited = set([cyc])
            dfs(cyc)
        print(dist[B])
