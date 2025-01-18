import sys

N, L = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0

for r in range(N):
    flag = 0
    prev = board[r][0]
    lst = []
    num = 0
    for c in range(N):
        if prev == board[r][c]:
            num += 1

        elif prev == board[r][c] - 1:
            lst.append(num)
            lst.append("UP")
            num = 1
        elif prev == board[r][c] + 1:
            lst.append(num)
            lst.append("DW")
            num = 1
        else:
            flag = 1
            break
        prev = board[r][c]

    lst.append(num)

    if flag:
        continue

    for i in range(len(lst)):
        if lst[i] == "UP":
            lst[i - 1] -= L
            if lst[i - 1] < 0:
                break
        elif lst[i] == "DW":
            lst[i + 1] -= L
            if lst[i + 1] < 0:
                break
    else:
        ans += 1


for c in range(N):
    flag = 0
    prev = board[0][c]
    lst = []
    num = 0
    for r in range(N):
        if prev == board[r][c]:
            num += 1

        elif prev == board[r][c] - 1:
            lst.append(num)
            lst.append("UP")
            num = 1
        elif prev == board[r][c] + 1:
            lst.append(num)
            lst.append("DW")
            num = 1
        else:
            flag = 1
            break
        prev = board[r][c]

    lst.append(num)

    if flag:
        continue

    for i in range(len(lst)):
        if lst[i] == "UP":
            lst[i - 1] -= L
            if lst[i - 1] < 0:
                break
        elif lst[i] == "DW":
            lst[i + 1] -= L
            if lst[i + 1] < 0:
                break
    else:
        ans += 1

print(ans)
