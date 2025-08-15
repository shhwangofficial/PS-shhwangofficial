import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N = int(input())
comm = list(map(int, input().split()))

deck = deque([i for i in range(N)])
ans = [0] * N
for i in range(N):
    if comm[i] == 1:
        idx = deck.popleft()
    elif comm[i] == 2:
        tmp = deck.popleft()
        idx = deck.popleft()
        deck.appendleft(tmp)
    else:
        idx = deck.pop()
    ans[idx] = N - i
print(*ans)
