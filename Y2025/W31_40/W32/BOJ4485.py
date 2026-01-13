import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
prob_no = 1
while True:
    N = int(input())
    if N == 0:
        exit()
    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float("inf")] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance[0][0] = board[0][0]
    heap = [(board[0][0], 0, 0)]
    while heap:
        dist, r, c = heapq.heappop(heap)
        if visited[r][c]:
            continue
        visited[r][c] = 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if board[nr][nc] + dist < distance[nr][nc]:
                    distance[nr][nc] = board[nr][nc] + dist
                    heapq.heappush(heap, (distance[nr][nc], nr, nc))
    print(f"Problem {prob_no}: {distance[N-1][N-1]}")
    prob_no += 1
