import sys
from collections import defaultdict
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    heap = []
    minus_heap = []
    dic = defaultdict(int)
    for i in range(k):
        c, num = map(str, sys.stdin.readline().split())
        num = int(num)
        if c == "I":
            heapq.heappush(heap, num)
            heapq.heappush(minus_heap, -num)
            dic[num] += 1
        elif num == -1:
            while heap:
                now = heapq.heappop(heap)
                if dic[now] > 0:
                    dic[now] -= 1
                    break
        elif num == 1:
            while minus_heap:
                now = heapq.heappop(minus_heap)
                if dic[-now] > 0:
                    dic[-now] -= 1
                    break
    while heap:
        now = heapq.heappop(heap)
        if dic[now] > 0:
            min_ = now
            break
    else:
        print("EMPTY")
        continue

    while minus_heap:
        now = heapq.heappop(minus_heap)
        if dic[-now] > 0:
            max_ = -now
            break
    else:
        print("EMPTY")
        continue
    
    print(max_, min_)
