import sys, heapq
N = int(sys.stdin.readline())
directed_by = [0 for i in range(N+1)]
visited = [0 for i in range(N+1)]
visited[0] = 1 
graph = [[] for i in range(N+1)]
for i in range(1, N+1):
    num = list(map(int, sys.stdin.readline().rstrip()))
    for j in range(len(num)):
        if num[j] == 1:
            directed_by[i] += 1
            graph[j+1].append(i)

minus_heap = []
for i in range(1, N+1):
    if directed_by[i] == 0:
        heapq.heappush(minus_heap, -i)
        
result = []
while minus_heap:
    now = -1 * heapq.heappop(minus_heap)
    visited[now] = 1
    result.append(now)
    for i in range(len(graph[now])):
        directed_by[graph[now][i]] -= 1
        if directed_by[graph[now][i]] == 0:
            heapq.heappush(minus_heap, -graph[now][i])
            
if 0 in visited:
    print(-1)
    exit(0)

result.reverse()
real_result = []
for i in range(1, N+1):
    for j in range(len(result)):
        if result[j] == i:
            real_result.append(j+1)
            break
print(*real_result)