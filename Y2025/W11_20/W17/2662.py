import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dp = [[0] * (M) for _ in range(N + 1)]
path = [[[]] * (M) for _ in range(N + 1)]

lst = [[0] * (M)]
for _ in range(N):
    lst.append(list(map(int, input().split()))[1:])

for c in range(M):
    if c == 0:
        for r in range(N + 1):
            dp[r][c] = lst[r][c]
            path[r][c] = [r]
        continue

    for add in range(0, N + 1):
        for r in range(N + 1):
            if r + add <= N:
                if dp[r + add][c] <= dp[r][c - 1] + lst[add][c]:
                    dp[r + add][c] = dp[r][c - 1] + lst[add][c]
                    path[r + add][c] = path[r][c - 1] + [add]
            else:
                break
ans = 0
for r in range(N + 1):
    if dp[r][-1] > ans:
        ans = dp[r][-1]
        pans = path[r][-1]

print(ans)
print(*pans)
