import heapq
import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [10000000] * (F + 1)
heap = [[0, S]]
visited[S] = 0
while heap:
    now = heapq.heappop(heap)
    if now[1] == G:
        print(now[0])
        break

    if now[1] + U <= F and now[0] + 1 < visited[now[1] + U]:
        heapq.heappush(heap, [now[0] + 1, now[1] + U])
        visited[now[1] + U] = now[0] + 1
    if now[1] - D >= 1 and now[0] + 1 < visited[now[1] - D]:
        heapq.heappush(heap, [now[0] + 1, now[1] - D])
        visited[now[1] - D] = now[0] + 1

else:
    print("use the stairs")
