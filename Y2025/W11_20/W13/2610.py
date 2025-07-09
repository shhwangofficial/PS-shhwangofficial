import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque


def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[py] = px


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    union(a, b)

committee = dict()
for n in range(1, N + 1):
    pn = find(n)
    if pn not in committee:
        committee[pn] = [n, float("inf")]
    visited = set([n])
    queue = deque([(n, 0)])
    while queue:
        now, step = queue.popleft()
        for nxt in graph[now]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, step + 1))
    if committee[pn][1] > step:
        committee[pn] = [n, step]

print(len(committee))
lst = []
for key in committee.keys():
    lst.append(committee[key][0])

for i in sorted(lst):
    print(i)
