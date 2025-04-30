import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dont_mix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    dont_mix[a][b] = 1
    dont_mix[b][a] = 1

ans = 0


def backtrack(lst):
    if len(lst) == 3:
        global ans
        ans += 1
        return

    for i in range(lst[-1] + 1, N + 1):
        for j in lst:
            if dont_mix[j][i] == 1:
                break
        else:
            backtrack(lst + [i])


for i in range(1, N + 1):
    backtrack([i])
print(ans)
