import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

boxes.sort(key=lambda x: x[1])

capacity = [C] * (N + 1)
total_lifted = 0
for i in range(len(boxes)):
    s, e, w = boxes[i]
    min_ = min(capacity[s:e])
    if min_ > 0:
        load = min(min_, w)
        total_lifted += load
        for j in range(s, e):
            capacity[j] -= load

print(total_lifted)
