import sys
import heapq

N = int(sys.stdin.readline())
max_heap = []
min_heap = []
solved = [0] * 100001
for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    heapq.heappush(max_heap, [-L, -P])
    heapq.heappush(min_heap, [L, P])
    solved[P] = L

M = int(sys.stdin.readline())
for _ in range(M):
    query = list(map(str, sys.stdin.readline().split()))
    if query[0] == "add":
        P, L = int(query[1]), int(query[2])
        heapq.heappush(max_heap, [-L, -P])
        heapq.heappush(min_heap, [L, P])
        solved[P] = L
    elif query[0] == "solved":
        solved[int(query[1])] = 0
    elif query[0] == "recommend":
        if query[1] == "1":
            while 1:
                L, P = heapq.heappop(max_heap)
                if solved[-P] == -L:
                    print(-P)
                    heapq.heappush(max_heap, [L, P])
                    break
        elif query[1] == "-1":
            while 1:
                L, P = heapq.heappop(min_heap)
                if solved[P] == L:
                    print(P)
                    heapq.heappush(min_heap, [L, P])
                    break
