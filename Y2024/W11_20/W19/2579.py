import sys

N = int(sys.stdin.readline())
steps = []
for i in range(N):
    steps.append(int(sys.stdin.readline()))
dp1 = [0, 0]
dp2 = [0, 0]
for i in range(2, N + 2):
    dp1.append(steps[i - 2] + dp2[i - 1])
    dp2.append(steps[i - 2] + max(dp1[i - 2], dp2[i - 2]))

print(max(dp1[-1], dp2[-1]))
