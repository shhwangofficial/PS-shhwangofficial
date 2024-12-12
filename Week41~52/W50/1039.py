import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

ans = 0
string_N = list(str(N))
visited = [[0] * (1000001) for _ in range(K + 1)]
queue = deque([(N, 0)])

while queue:
    num, turn = queue.popleft()
    string_num = list(str(num))
    for i in range(len(string_num)):
        for j in range(i + 1, len(string_num)):
            if i == 0 and string_num[j] == "0":
                continue
            string_num[i], string_num[j] = string_num[j], string_num[i]
            temp = int("".join((string_num)))
            if turn == K - 1:
                ans = max(ans, temp)
            elif visited[turn + 1][temp] == 0:
                visited[turn + 1][temp] = 1
                queue.append((temp, turn + 1))
            string_num[i], string_num[j] = string_num[j], string_num[i]


print(ans if ans != 0 else -1)
