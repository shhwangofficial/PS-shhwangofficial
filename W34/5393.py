import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    if N % 2 == 0:
        ans = 1
        ans += N - ((N + 2) // 2)
        ans += (N - ((N - 1) // 3 + 1) + 1) // 2
    else:
        ans = 2
        ans += N - ((N + 1) // 2)
        ans += (N - (((N - 1) // 3) + 1)) // 2
    print(ans)
