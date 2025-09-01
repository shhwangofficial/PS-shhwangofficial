import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
dp = [[float("inf")] * (N) for _ in range(1 << N)]
dp[1][0] = 0
for dpr in range(1, (1 << N) - 1):
    for dpc in range(N):
        if dp[dpr][dpc] != float("inf"):
            for buyer in range(N):
                bit = 1 << buyer
                if not (dpr & bit) and dp[dpr][dpc] <= board[dpc][buyer]:
                    dp[dpr | bit][buyer] = min(board[dpc][buyer], dp[dpr | bit][buyer])

ans = 0
for r in range((1 << N) - 1, -1, -1):
    if min(dp[r]) != float("inf"):
        temp = 0
        for i in range(N):
            if r & (1 << i):
                temp += 1
        ans = max(ans, temp)

print(ans)
