import sys
import math
from collections import deque

n, k = map(int, sys.stdin.readline().split())

dots = []
dots.append([0, 0])
for i in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))
dots.append([10000, 10000])

dist = [[0] * len(dots) for _ in range(len(dots))]
for i in range(len(dots)):
    for j in range(len(dots)):
        distance = ((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2) ** 0.5
        dist[i][j] = math.ceil(distance / 10)

s, e = 1, 1500
while s <= e:
    mid = (s + e) // 2
    visited = [0] * len(dots)
    visited[0] = 1
    queue = deque([(0, 0)])
    while queue:
        now, step = queue.popleft()
        if now == len(dots) - 1:
            e = mid - 1
            temp = mid
            break
        for i in range(len(dots)):
            if visited[i] == 0 and dist[now][i] <= mid and step <= k:
                visited[i] = 1
                queue.append((i, step + 1))
    else:
        s = mid + 1

print(temp)
