import sys, heapq

N = int(sys.stdin.readline())
dig = [(int(sys.stdin.readline()), i) for i in range(N)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heapq.heapify(dig)
heap = dig

distance = [float("inf")] * N
connected = [0] * N
cnt = 0
ans = 0
while heap:
    cost, now = heapq.heappop(heap)
    if connected[now] == 0:
        connected[now] = 1
        ans += cost
        cnt += 1
        if cnt == N:
            break
        for i in range(N):
            if connected[i] == 0 and graph[now][i] < distance[i]:
                distance[i] = graph[now][i]
                heapq.heappush(heap, (distance[i], i))

print(ans)
