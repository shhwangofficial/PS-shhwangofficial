import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10001)


def dfs(node):
    set_ = set([node])
    for nxt in graph[node]:
        set_ = set_.union(dfs(nxt))
    if x in set_ and y in set_:
        print(node)
        return set([])
    return set_


T = int(input())
for _ in range(T):
    N = int(input())
    root = set(range(1, N + 1))
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        A, B = map(int, input().split())
        root.discard(B)
        graph[A].append(B)
    x, y = map(int, input().split())
    dfs(root.pop())
