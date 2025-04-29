import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
if 2 <= N <= 4:
    graph = [[0] * N for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1
    ans = []
    for r in range(N):
        for c in range(N):
            if r != c and graph[r][c] == 0:
                graph[r][c] = 1
                graph[c][r] = 1
                ans.append([r + 1, c + 1])
    print(len(ans))
    print(1)
    for a in ans:
        print(*a)

else:
    conn_with_one = [0] * (N + 1)
    conn_with_one[1] = 1
    for _ in range(N - 1):
        a, b = map(int, input().split())
        if a == 1:
            conn_with_one[b] = 1
        elif b == 1:
            conn_with_one[a] = 1

    ans = []
    for i in range(2, N + 1):
        if conn_with_one[i] == 0:
            ans.append([1, i])

    print(len(ans))
    print(2)
    for a in ans:
        print(*a)
