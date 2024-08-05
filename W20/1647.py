import heapq
import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

connected = [0 for i in range(N + 1)]  # 트리에 포함되었는지 확인하는 배열

heap = [(0, 1)]  # 아무 노드로 시작해도 됨

sum_ = 0
max_ = 0
num_lines = 0
while heap:
    now = heapq.heappop(heap)

    if connected[now[1]] == 0:  # 연결이 기존에 안되어있을 때만 아래를 진행한다.

        connected[now[1]] = 1
        sum_ += now[0]
        max_ = max(now[0], max_)
        if num_lines == N - 1:
            break
        num_lines += 1
        for line in graph[now[1]]:
            if connected[line[0]] == 0:
                heapq.heappush(heap, (line[1], line[0]))

print(sum_ - max_)
