import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    fr, to = map(int, sys.stdin.readline().split())
    visited = [999999] * 10000
    visited_command = [""] * 10000
    visited[fr] = 0
    queue = deque([(fr, 0)])
    while queue:
        now, t = queue.popleft()
        if now == to:
            print(visited_command[to])
            break
        nowC = visited_command[now]
        D = (now * 2) % 10000
        if visited[D] > t + 1:
            visited[D] = t + 1
            visited_command[D] = nowC + "D"
            queue.append((D, t + 1))
        S = (now - 1) % 10000
        if visited[S] > t + 1:
            visited[S] = t + 1
            visited_command[S] = nowC + "S"
            queue.append((S, t + 1))
        L = (now % 1000) * 10 + (now // 1000)
        if visited[L] > t + 1:
            visited[L] = t + 1
            visited_command[L] = nowC + "L"
            queue.append((L, t + 1))
        R = (now // 10) + ((now % 10) * 1000)
        if visited[R] > t + 1:
            visited[R] = t + 1
            visited_command[R] = nowC + "R"
            queue.append((R, t + 1))
