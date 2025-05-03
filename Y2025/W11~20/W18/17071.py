import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, K = map(int, input().split())

subin_odd = [-1] * 500001
subin_even = [-1] * 500001
brother = [-1] * 500001
subin_even[N] = 0
queue = deque([(N, 0)])
while queue:
    now, time = queue.popleft()
    for nxt in (now + 1, now - 1, 2 * now):
        if 0 <= nxt <= 500000:
            if (time + 1) % 2:
                if subin_odd[nxt] == -1:
                    subin_odd[nxt] = time + 1
                    queue.append((nxt, time + 1))
            else:
                if subin_even[nxt] == -1:
                    subin_even[nxt] = time + 1
                    queue.append((nxt, time + 1))

t = 0

while True:
    K += t
    if K <= 500000:
        if t % 2:
            if subin_odd[K] <= t:
                print(t)
                break
        else:
            if subin_even[K] <= t:
                print(t)
                break
        t += 1
    else:
        print(-1)
        break
