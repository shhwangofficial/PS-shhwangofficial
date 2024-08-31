import sys

T = int(sys.stdin.readline())
Inf = 10**8
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[Inf] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        graph[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = c
        graph[b][a] = c
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    K = int(sys.stdin.readline())
    friends = list(map(int, sys.stdin.readline().split()))
    min_ = Inf
    temp_place = 0
    for k in range(1, N + 1):
        temp_cost = 0
        for friend in friends:
            temp_cost += graph[friend][k]
        if min_ > temp_cost:
            min_ = temp_cost
            temp_place = k
    print(temp_place)
