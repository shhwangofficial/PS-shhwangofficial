import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
check = [w, v, u, t, s, r, q, p, o, n, m]
board = [
    [
        [
            [
                [
                    [
                        [
                            [[[list(map(int, input().split())) for _ in range(n)] for _ in range(o)] for _ in range(p)]
                            for _ in range(q)
                        ]
                        for _ in range(r)
                    ]
                    for _ in range(s)
                ]
                for _ in range(t)
            ]
            for _ in range(u)
        ]
        for _ in range(v)
    ]
    for _ in range(w)
]

queue = deque([])
for W in range(w):
    for V in range(v):
        for U in range(u):
            for T in range(t):
                for S in range(s):
                    for R in range(r):
                        for Q in range(q):
                            for P in range(p):
                                for O in range(o):
                                    for N in range(n):
                                        for M in range(m):
                                            if board[W][V][U][T][S][R][Q][P][O][N][M] == 1:
                                                queue.append([W, V, U, T, S, R, Q, P, O, N, M, 0])

delta = [-1, 1]
ans = 0
while queue:
    now = queue.popleft()
    ans = max(now[-1], ans)
    for d in delta:
        for dim in range(11):
            new = now[:-1]
            new[dim] += d
            if 0 <= new[dim] < check[dim]:
                W, V, U, T, S, R, Q, P, O, N, M = new
                if board[W][V][U][T][S][R][Q][P][O][N][M] == 0:
                    board[W][V][U][T][S][R][Q][P][O][N][M] = 1
                    queue.append(new[:] + [now[-1] + 1])


for W in range(w):
    for V in range(v):
        for U in range(u):
            for T in range(t):
                for S in range(s):
                    for R in range(r):
                        for Q in range(q):
                            for P in range(p):
                                for O in range(o):
                                    for N in range(n):
                                        for M in range(m):
                                            if board[W][V][U][T][S][R][Q][P][O][N][M] == 0:
                                                print(-1)
                                                exit()

print(ans)
