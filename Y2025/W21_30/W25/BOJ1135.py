import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for i in range(1, N):
    graph[tree[i]].append(i)


def dfs(now):
    if not graph[now]:
        return 0
    lst = []
    for nxt in graph[now]:
        lst.append(dfs(nxt))
    lst.sort(reverse=True)
    for i in range(len(lst)):
        lst[i] += i + 1
    return max(lst)


print(dfs(0))
