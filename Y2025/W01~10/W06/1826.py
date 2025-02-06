import sys
import heapq

N = int(sys.stdin.readline())

station = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    station.append((a, b))
L, P = map(int, sys.stdin.readline().split())
station.sort(key=lambda x: (x[0], -x[1]))
station.append((L, 0))

heap = []
cnt = 0
for a, b in station:
    while P < a and heap:
        P += -heapq.heappop(heap)
        cnt += 1
    if P >= L or P < a:
        break
    heapq.heappush(heap, -b)

print(cnt if P >= L else -1)
