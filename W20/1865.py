import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append([a, b, c])
        edges.append([b, a, c])
    for i in range(W):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append([a, b, -c])

    flag = False
    dist = [0 for _ in range(N + 1)]
    for i in range(N):
        print(dist)
        for j in range(len(edges)):
            curr_node = edges[j][0]
            next_node = edges[j][1]
            cost_edge = edges[j][2]
            if dist[next_node] > dist[curr_node] + cost_edge:
                if i == N - 1:
                    flag = True
                dist[next_node] = dist[curr_node] + cost_edge

    if flag:
        print("YES")
    else:
        print("NO")
