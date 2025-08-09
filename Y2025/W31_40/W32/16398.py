import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
heap = [(0, 0)]
ans = 0
while heap:
    branch, now = heapq.heappop(heap)
    if visited[now]:
        continue
    visited[now] = 1
    ans += branch
    for i in range(N):
        if not visited[i]:
            heapq.heappush(heap, (graph[now][i], i))
print(ans)
