import sys
import heapq

inf = 10**9

T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    s, g, h = map(int, sys.stdin.readline().split())
    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
        if (a == g and b == h) or (b == g and a == h):
            g_h = d

    cands = set()
    for i in range(t):
        a = int(sys.stdin.readline())
        cands.add(a)

    cands_temp = {i for i in cands}
    min_dist = [inf] * (n + 1)
    min_dist[s] = 0
    heap = [[0, s]]
    while heap:
        dist, now = heapq.heappop(heap)
        cands_temp.discard(now)
        if not cands_temp:
            break
        for line in graph[now]:
            if min_dist[line[0]] > line[1] + dist:
                min_dist[line[0]] = line[1] + dist
                heapq.heappush(heap, [min_dist[line[0]], line[0]])

    cands_temp = {i for i in cands}
    min_dist2 = [inf] * (n + 1)
    min_dist2[h] = 0
    heap = [[0, h]]
    while heap:
        dist, now = heapq.heappop(heap)
        cands_temp.discard(now)
        if not cands_temp:
            break
        for line in graph[now]:
            if min_dist2[line[0]] > line[1] + dist:
                min_dist2[line[0]] = line[1] + dist
                heapq.heappush(heap, [min_dist2[line[0]], line[0]])

    cands_temp = {i for i in cands}
    min_dist3 = [inf] * (n + 1)
    min_dist3[g] = 0
    heap = [[0, g]]
    while heap:
        dist, now = heapq.heappop(heap)
        cands_temp.discard(now)
        if not cands_temp:
            break
        for line in graph[now]:
            if min_dist3[line[0]] > line[1] + dist:
                min_dist3[line[0]] = line[1] + dist
                heapq.heappush(heap, [min_dist3[line[0]], line[0]])

    ans = []
    for i in cands:
        if (min_dist[g] + min_dist2[i] + g_h == min_dist[i]) or (min_dist[h] + min_dist3[i] + g_h == min_dist[i]):
            ans.append(i)
    print(*sorted(ans))
