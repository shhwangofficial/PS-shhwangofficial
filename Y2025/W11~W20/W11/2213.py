import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

n = int(input())
weights = [0] + list(map(int, input().split()))
previous = [0]
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [weights[:], [0] * (n + 1)]
track = [[[i] for i in range(n + 1)], [[] for _ in range(n + 1)]]

visited = set([1])
stack = [(0, 1)]
while stack:
    prev, now = stack[-1]
    for nxt in graph[now]:
        if nxt not in visited:
            visited.add(nxt)
            stack.append((now, nxt))
            break
    else:
        prev, now = stack.pop()
        if dp[0][now] > dp[1][now]:
            dp[1][prev] += dp[0][now]
            track[1][prev] += track[0][now]
        else:
            dp[1][prev] += dp[1][now]
            track[1][prev] += track[1][now]

        dp[0][prev] += dp[1][now]
        track[0][prev] += track[1][now]


if dp[0][1] > dp[1][1]:
    print(dp[0][1])
    print(*sorted(track[0][1]))
else:
    print(dp[1][1])
    print(*sorted(track[1][1]))
