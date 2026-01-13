import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
exploded = [0, 0, 0, 0]


def blizzard(bdir, blen):
    r, c = N // 2, N // 2
    for length in range(1, blen + 1):
        nr, nc = r + dr[bdir] * length, c + dc[bdir] * length
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] = 0


def burst(lst):
    while True:
        i = 0
        cnt = 0
        flag = 0
        stack = []
        while i < len(lst):
            if i == 0:
                before = lst[0]
                cnt = 1
            elif before == lst[i]:
                cnt += 1
            elif before != lst[i]:
                if cnt >= 4:
                    stack.append((i - cnt, i))
                    exploded[before] += cnt
                    flag = 1
                before = lst[i]
                cnt = 1
            i += 1
        if cnt >= 4:
            stack.append((i - cnt, i))
            exploded[before] += cnt
            flag = 1
        if flag:
            while stack:
                fr, to = stack.pop()
                lst = lst[:fr] + lst[to:]
        else:
            break

    if cnt >= 4:
        lst = lst[: i - cnt] + lst[i:]
        exploded[before] += cnt

    return lst


def fill(lst):
    dim = 3
    r, c = N // 2, N // 2
    idx = 0
    while dim <= N:
        for dir, amount in ((3, 1), (2, dim - 2), (4, dim - 1), (1, dim - 1), (3, dim - 1)):
            for a in range(amount):
                r, c = r + dr[dir], c + dc[dir]
                board[r][c] = lst[idx]
                idx += 1
                if idx == len(lst):
                    return

        dim += 2
    return


def shift():
    dim = 3
    r, c = N // 2, N // 2
    lst = []
    while dim <= N:
        for dir, amount in ((3, 1), (2, dim - 2), (4, dim - 1), (1, dim - 1), (3, dim - 1)):
            for a in range(amount):
                r, c = r + dr[dir], c + dc[dir]
                if board[r][c] != 0:
                    lst.append(board[r][c])
                board[r][c] = 0
        dim += 2

    return burst(lst)


def expand(lst):
    global board
    board = [[0] * N for _ in range(N)]
    if not lst:
        return

    new_lst = []
    i = 0
    while i < len(lst):
        if i == 0:
            before = lst[0]
            cnt = 1
            i += 1
            continue
        if before == lst[i]:
            cnt += 1
            i += 1
        elif before != lst[i]:
            new_lst.append(cnt)
            new_lst.append(lst[i - 1])
            before = lst[i]
            i += 1
            cnt = 1

    new_lst.append(cnt)
    new_lst.append(lst[i - 1])

    fill(new_lst)


for _ in range(M):
    bdir, blen = map(int, sys.stdin.readline().split())
    blizzard(bdir, blen)
    lst = shift()
    expand(lst)

ans = 0
for i, val in enumerate(exploded):
    ans += i * val
print(ans)
