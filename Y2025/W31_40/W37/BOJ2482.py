import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
K = int(input())

if K > N // 2:
    print(0)
    exit()

if K == 1:
    print(N)
    exit()

MOD = 1000000003

sel = [[0] * (K + 1) for _ in range(N + 1)]
unsel = [[0] * (K + 1) for _ in range(N + 1)]
unsel[0][0] = 1
sel[1][1] = 1
unsel[1][0] = 1
for i in range(2, N + 1):
    for j in range(K + 1):
        if sel[i - 1][j]:
            unsel[i][j] = (unsel[i][j] + sel[i - 1][j]) % MOD
        if unsel[i - 1][j]:
            unsel[i][j] = (unsel[i][j] + unsel[i - 1][j]) % MOD
            if j != K:
                sel[i][j + 1] = (sel[i][j + 1] + unsel[i - 1][j]) % MOD

print((unsel[N][K] + sel[N][K] - unsel[N - 4][K - 2] - sel[N - 4][K - 2]) % MOD)
