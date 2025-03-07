import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(1, T + 1):
    K, M, P = map(int, input().split())
    directed = [0] * M
    order = [0] * M
    cnt = [1] * M
    graph = [[] for _ in range(M)]
    for _ in range(P):
        A, B = map(lambda x: int(x) - 1, input().split())
        directed[B] += 1
        graph[A].append(B)
    now = []
    cand = []
    for node in range(M):
        if directed[node] == 0:
            now.append(node)
            order[node] = 1

    flag = 0
    while now:
        for node in now:
            for nxt in graph[node]:
                if order[node] > order[nxt]:
                    cnt[nxt] = 1
                    order[nxt] = order[node]
                elif order[node] == order[nxt]:
                    cnt[nxt] += 1
                directed[nxt] -= 1
                if directed[nxt] == 0:
                    if cnt[nxt] > 1:
                        order[nxt] += 1
                    cand.append(nxt)

        now = cand[:]
        cand = []
    print(K, order[M - 1])
