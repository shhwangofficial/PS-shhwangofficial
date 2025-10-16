import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
tank = list(map(int, input().split()))


def check():
    max_, min_ = tank[0], tank[0]
    for i in range(1, N):
        max_ = max(max_, tank[i])
        min_ = min(min_, tank[i])
    if max_ - min_ <= K:
        return True
    return False


def put_fish():
    tmp = float("inf")
    ans = []
    for i in range(N):
        if tmp > tank[i]:
            tmp = tank[i]
            ans = [i]
        elif tmp == tank[i]:
            ans.append(i)
    for i in ans:
        tank[i] += 1


def buyang_90():
    top = [[tank[0]]]
    top_height = 1
    top_base = 1
    tail_start = 2
    while top_height + 1 <= N - tail_start:
        new_top = [[0] * (top_height + 1) for _ in range(top_base)]
        for r in range(top_base):
            new_top[r][0] = tank[tail_start - top_base + r]
        for r in range(top_height):
            for c in range(top_base):
                new_top[c][top_height - r] = top[r][c]
        tail_start += top_height + 1
        top_base, top_height = top_height + 1, top_base
        top = new_top

    return top, tail_start - top_base


def spread(top, tank_start, isfirst=1):
    row_top, col_top = len(top), len(top[0])
    offset = [[0] * col_top for _ in range(row_top)]
    end = N if isfirst else N // 4
    offset.append([0] * (end - tank_start))
    for r in range(row_top):
        for c in range(col_top - 1):
            now = top[r][c]
            nxt = top[r][c + 1]
            diff = (nxt - now) // 5
            if diff < 0 and (now - nxt) % 5:
                diff += 1
            offset[r][c] += diff
            offset[r][c + 1] -= diff

    for r in range(row_top - 1):
        for c in range(col_top):
            now = top[r][c]
            nxt = top[r + 1][c]
            diff = (nxt - now) // 5
            if diff < 0 and (now - nxt) % 5:
                diff += 1
            offset[r][c] += diff
            offset[r + 1][c] -= diff

    for c in range(tank_start, end - 1):
        now = tank[c]
        nxt = tank[c + 1]
        diff = (nxt - now) // 5
        if diff < 0 and (now - nxt) % 5:
            diff += 1
        offset[-1][c - tank_start] += diff
        offset[-1][c - tank_start + 1] -= diff
    for c in range(col_top):
        now = top[-1][c]
        nxt = tank[c + tank_start]
        diff = (nxt - now) // 5
        if diff < 0 and (now - nxt) % 5:
            diff += 1
        offset[-2][c] += diff
        offset[-1][c] -= diff

    for r in range(row_top):
        for c in range(col_top):
            top[r][c] += offset[r][c]
    for c in range(tank_start, end):
        tank[c] += offset[-1][c - tank_start]

    return tank, top, tank_start


def linear(tank, top, tank_start):
    row_top, col_top = len(top), len(top[0])
    new_tank = []
    for i in range(col_top):
        new_tank.append(tank[tank_start + i])
        for r in range(row_top - 1, -1, -1):
            new_tank.append(top[r][i])
    for i in range(tank_start + col_top, N):
        new_tank.append(tank[i])
    return new_tank


def buyang_180():
    new_tank = [[0] * (N // 4) for _ in range(4)]
    for i in range(N // 4):
        new_tank[2][N // 4 - i - 1] = tank[i]
    for i in range(N // 4, 2 * N // 4):
        new_tank[1][i - N // 4] = tank[i]
    for i in range(2 * N // 4, 3 * N // 4):
        new_tank[0][3 * N // 4 - i - 1] = tank[i]
    for i in range(3 * N // 4, N):
        new_tank[3][i - 3 * N // 4] = tank[i]
    return new_tank


def linear2():
    new_tank = []
    for c in range(N // 4):
        for r in range(4 - 1, -1, -1):
            new_tank.append(tank[r][c])
    return new_tank


ans = 0
while True:
    if check():
        break
    ans += 1
    put_fish()
    top, tank_start = buyang_90()
    tank, top, tank_start = spread(top, tank_start)
    tank = linear(tank, top, tank_start)
    tank = buyang_180()
    top, tank = tank[:-1], tank[-1]
    tank, top, tank_start = spread(top, 0, 0)
    tank = top + [tank]
    tank = linear2()

print(ans)
