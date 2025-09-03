import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K, M = map(int, input().split())
from collections import defaultdict, deque

dic = defaultdict(list)
graph_lst = []
for i in range(M):
    line = list(map(int, input().split()))
    graph_lst.append(line)
    for station in line:
        dic[station].append(i)

queue = deque([(1, 1)])
visited = [0] * (N + 1)

while queue:
    step, now = queue.popleft()
    if now == N:
        print(step)
        break
    for graph_no in dic[now]:
        for nxt in graph_lst[graph_no]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append((step + 1, nxt))
else:
    print(-1)
