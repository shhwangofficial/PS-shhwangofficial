import sys
from collections import deque, defaultdict

board = ""
for _ in range(3):
    a, b, c = map(str, sys.stdin.readline().split())
    board += a + b + c

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dic = defaultdict(int)
dic[board] = 1
queue = deque([[board, 1]])
while queue:
    now, move = queue.popleft()
    if now == "123456780":
        break
    loc0 = now.index("0")
    for i in range(4):
        nr, nc = loc0 // 3 + dx[i], loc0 % 3 + dy[i]
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_now = list(now)
            temp = new_now[nr * 3 + nc]
            new_now[nr * 3 + nc] = "0"
            new_now[loc0] = temp
            new_now = "".join(new_now)
            if not dic[new_now]:
                dic[new_now] = move + 1
                queue.append([new_now, move + 1])

print(dic["123456780"] - 1)
