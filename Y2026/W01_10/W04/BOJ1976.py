import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
tour = list(map(int, input().split()))

visited = [0] * N
dic = dict()
index = 0
for i in range(N):
    if visited[i] == 0:
        index += 1
        dic[index] = set()
        visited[i] = 1
        stack = [i]
        while stack:
            now = stack.pop()
            dic[index].add(now)
            for j in range(N):
                if board[now][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    stack.append(j)

start = tour[0] - 1
conn = 0
for i in range(1, index + 1):
    if start in dic[i]:
        conn = i
        break

if conn:
    for t in tour:
        if t - 1 not in dic[conn]:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
