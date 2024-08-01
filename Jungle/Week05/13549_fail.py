import sys, heapq
a, b = map(int,sys.stdin.readline().split())

heap = [[0,b]]

while heap:
    now = heapq.heappop(heap)
    if now[1] == a:
        print(now[0])
        break
    elif now[1] < a:
        heapq.heappush(heap, [now[0]+a-now[1], a])
        continue
    else:
        if now[1] % 2 == 0:
            heapq.heappush(heap, [now[0], now[1]//2])
        heapq.heappush(heap, [now[0]+1, now[1]+1])
        heapq.heappush(heap, [now[0]+1, now[1]-1])

