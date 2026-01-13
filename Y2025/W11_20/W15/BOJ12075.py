import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(1, T + 1):
    K = int(input())
    rev = 1
    while K:
        if K == 1:
            break
        n = 1
        while True:
            if 2 ** (n - 1) - 1 < K <= 2**n - 1:
                break
            n += 1
        if K == 2 ** (n - 1):
            break
        else:
            rev *= -1
            K = 2**n - 1 - K + 1

    ans = 1 if rev == -1 else 0
    print(f"Case #{t}: {ans}")
