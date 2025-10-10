import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(200001)

N = int(input())
nal = [0] + list(map(int, input().split()))
graph = [[] for i in range(N + 1)]
for i, p in enumerate(map(int, input().split())):
    graph[p].append(i + 2)

dp = [[0, 0] for i in range(N + 1)]  # dp[v][0]: v 선택안함, dp[v][1]: v 선택함


def dfs(u):
    dp[u][1] = nal[u]
    for v in graph[u]:
        dfs(v)
        dp[u][0] += max(dp[v][0], dp[v][1])
        dp[u][1] += dp[v][0]


def track(u, last):
    if not last:
        if dp[u][0] < dp[u][1]:
            lst.append(u)
            last = True
    else:
        last = False
    for v in graph[u]:
        track(v, last)


dfs(1)
print(dp[1][1], dp[1][0])

lst = []
lst.append(1)
for v in graph[1]:
    track(v, True)
print(*sorted(lst), end=" ")
print(-1)

lst = []
track(1, True)
print(*sorted(lst), end=" ")
print(-1)
