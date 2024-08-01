import sys
N, M, K = map(int,sys.stdin.readline().split())
infected = set(list(map(int, sys.stdin.readline().split())))
graph = []
for i in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))
graph.sort()
for suspect in infected:
    sus = set([suspect])
    for i in range(len(graph)):
        if graph[i][1] in sus:
            sus.add(graph[i][2])
    if sus == infected:
        print(suspect)
        exit()

