import sys, heapq

N, k = map(int, sys.stdin.readline().split())

heap = [[0, i] for i in range(1, k + 1)]

customers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = []
for id, items in customers:
    wait, casher = heapq.heappop(heap)
    ans.append([wait + items, casher, id])
    heapq.heappush(heap, [wait + items, casher])

ans.sort(key=lambda x: (x[0], -x[1]))

sum_ = 0
for i in range(N):
    sum_ += (i + 1) * ans[i][2]

print(sum_)
