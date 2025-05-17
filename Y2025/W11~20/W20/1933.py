import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

N = int(input())
find_end = [0] * (N + 1)
spots = []
for i in range(1, N + 1):
    s, h, e = map(int, input().split())
    spots.append((s, i, 1))
    spots.append((e, i, 0))
    find_end[i] = (-h, e)

spots.sort(key=lambda x: (x[0], -x[2], find_end[x[1]][0]))

ans = []
now = 0
heap = []
check = set()
for x, i, is_start in spots:
    if is_start:
        if now < -find_end[i][0]:
            ans.append((x, -find_end[i][0]))
            now = -find_end[i][0]
        heapq.heappush(heap, find_end[i])

    else:  # 끝점
        check.add(x)
        while heap:
            if heap[0][1] not in check:
                break
            heapq.heappop(heap)
        if not heap:
            if now != 0:
                now = 0
                ans.append((x, now))
        else:
            if now != -heap[0][0]:
                now = -heap[0][0]
                ans.append((x, now))

for x, h in ans:
    print(x, h, end=" ")
