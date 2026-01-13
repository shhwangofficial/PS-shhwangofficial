import copy
import sys

N = int(sys.stdin.readline())
ground_origin = []
for _ in range(N):
    ground_origin.append(list(map(int, sys.stdin.readline().split())))

max_ = 0


def play(ground, round):
    if round == 5:
        global max_
        for i in range(N):
            for j in range(N):
                if ground[i][j] > max_:
                    max_ = ground[i][j]
        return

    # left
    ground_new = copy.deepcopy(ground)
    for i in range(N):
        p1 = 0
        p2 = 1
        while p2 < N:
            if ground_new[i][p2] == 0:
                p2 += 1
                continue
            elif ground_new[i][p1] == 0 and ground_new[i][p2] > 0:
                ground_new[i][p1], ground_new[i][p2] = (
                    ground_new[i][p2],
                    ground_new[i][p1],
                )
                continue
            elif ground_new[i][p1] == ground_new[i][p2]:
                ground_new[i][p1] *= 2
                ground_new[i][p2] = 0
            p1 += 1
            p2 = p1 + 1
    play(ground_new, round + 1)

    # right
    ground_new = copy.deepcopy(ground)
    for i in range(N):
        p1 = N - 1
        p2 = N - 2
        while p2 >= 0:
            if ground_new[i][p2] == 0:
                p2 -= 1
                continue
            elif ground_new[i][p1] == 0 and ground_new[i][p2] > 0:
                ground_new[i][p1], ground_new[i][p2] = (
                    ground_new[i][p2],
                    ground_new[i][p1],
                )
                continue
            elif ground_new[i][p1] == ground_new[i][p2]:
                ground_new[i][p1] *= 2
                ground_new[i][p2] = 0
            p1 -= 1
            p2 = p1 - 1
    play(ground_new, round + 1)

    # up
    ground_new = copy.deepcopy(ground)
    for i in range(N):
        p1 = 0
        p2 = 1
        while p2 < N:
            if ground_new[p2][i] == 0:
                p2 += 1
                continue
            elif ground_new[p1][i] == 0 and ground_new[p2][i] > 0:
                ground_new[p1][i], ground_new[p2][i] = (
                    ground_new[p2][i],
                    ground_new[p1][i],
                )
                continue
            elif ground_new[p1][i] == ground_new[p2][i]:
                ground_new[p1][i] *= 2
                ground_new[p2][i] = 0
            p1 += 1
            p2 = p1 + 1
    play(ground_new, round + 1)

    # down
    ground_new = copy.deepcopy(ground)
    for i in range(N):
        p1 = N - 1
        p2 = N - 2
        while p2 >= 0:
            if ground_new[p2][i] == 0:
                p2 -= 1
                continue
            elif ground_new[p1][i] == 0 and ground_new[p2][i] > 0:
                ground_new[p1][i], ground_new[p2][i] = (
                    ground_new[p2][i],
                    ground_new[p1][i],
                )
                continue
            elif ground_new[p1][i] == ground_new[p2][i]:
                ground_new[p1][i] *= 2
                ground_new[p2][i] = 0
            p1 -= 1
            p2 = p1 - 1
    play(ground_new, round + 1)


play(ground_origin, 0)
print(max_)
