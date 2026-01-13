import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(node):
    bit = 0
    for nxt in graph[node]:
        if visited[nxt]:
            bit |= visited[nxt]
        else:
            bit |= dfs(nxt)
    visited[node] = bit | (1 << node)
    return visited[node]


visited = [0] * (n + 1)
for node in range(1, n + 1):
    dfs(node)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if (1 << a) & visited[b]:
        print(1)
    elif (1 << b) & visited[a]:
        print(-1)
    else:
        print(0)
