import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
long_path = [[] for _ in range(N)]


def dfs(now, visited):
    if visited == (1 << N) - 1:
        return [now]

    if long_path[now]:
        return long_path[now]

    ret = []
    ret_nxt = 0
    for nxt in range(1, N):
        if graph[now][nxt] and not visited & (1 << nxt):
            tmp = dfs(nxt, visited | (1 << nxt))
            if len(tmp) > len(ret):
                ret = tmp[:]
                ret_nxt = nxt

    long_path[now] = [ret_nxt] + ret
    return long_path[now]


dfs(0, 1)
print(len(long_path[0]))
print(1, end=" ")
for i in range(len(long_path[0]) - 1):
    print(long_path[0][i] + 1, end=" ")
