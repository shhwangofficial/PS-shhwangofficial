import sys
INF = int(1e9)
# 노드의 개수, 간선의 개수
N, M = map(int,sys.stdin.readline().split())
edges = []  # 벨만포드의 주인공은 간선임. 노드가 아니라
for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    edges.append([a, b, c])     # a->b, cost c


start = 1  # 다익스트라처럼 시작 노드를 정해주자
flag = True
dist = [INF for _ in range(N+1)]
dist[start] = 0
for i in range(N):  # 전체 N번의 round를 반복
    for j in range(M):  # 매 반복마다 "모든 간선을 확인"
        curr_node = edges[j][0]
        next_node = edges[j][1]
        cost_edge = edges[j][2]
        # 현재 간선(j번째)을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 -> 갱신
        if dist[curr_node] != INF and dist[next_node] > dist[curr_node] + cost_edge:
            if i == N - 1: # N번째 라운드에서도 값이 갱신 되었다면 음수 순환이 존재
                flag = False
            dist[next_node] = dist[curr_node] + cost_edge
            

if flag:
    for i in range(2, len(dist)):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
else: 
    print(-1)