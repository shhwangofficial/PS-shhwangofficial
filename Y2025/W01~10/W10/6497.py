import heapq

import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [[] for _ in range(m)]
    total_dist = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        total_dist += z
        graph[x].append((y, z))
        graph[y].append((x, z))
    connected = [0] * m
    connected_cnt = 0
    connected_sum = 0
    heap = [(0, 0)]
    while heap:
        cst, now = heapq.heappop(heap)
        if connected[now]:
            continue
        connected_cnt += 1
        connected[now] = 1
        connected_sum += cst
        if connected_cnt == m:
            print(total_dist - connected_sum)
            break

        for nxt, cst in graph[now]:
            if not connected[nxt]:
                heapq.heappush(heap, (cst, nxt))
