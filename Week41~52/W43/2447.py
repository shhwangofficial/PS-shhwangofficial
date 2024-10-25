import sys

N = int(sys.stdin.readline())


def solve(N):
    if N == 1:
        return ["*"]
    else:
        ret = []
        lower = solve(N // 3)
        for i in range(len(lower)):
            ret.append(lower[i] * 3)
        for i in range(len(lower)):
            ret.append(lower[i] + (" " * (N // 3)) + lower[i])
        for i in range(len(lower)):
            ret.append(lower[i] * 3)
        return ret


for line in solve(N):
    print(line)
