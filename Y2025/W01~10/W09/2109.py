import heapq

n = int(input())
heap = []
lst = [0] * 10001
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(heap, (-p, d))


while heap:
    p, d = heapq.heappop(heap)
    p = -p
    for i in range(d, 0, -1):
        if lst[i] == 0:
            lst[i] = p
            break


print(sum(lst))
