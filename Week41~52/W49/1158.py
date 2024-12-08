import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

queue = deque(range(1, a + 1))


i = 0
ans = []
while queue:
    now = queue.popleft()
    if i == b - 1:
        ans.append(now)
    else:
        queue.append(now)
    i = (i + 1) % b

print("<", end="")
print(*ans, sep=", ", end="")
print(">")
