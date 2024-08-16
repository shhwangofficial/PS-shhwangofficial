import sys

row, col = map(int, sys.stdin.readline().split())
board = []
for i in range(row):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(row):
    for j in range(col):
        if board[i][j] == "R":
            red = [i, j]
            board[i][j] = "."
            continue
        if board[i][j] == "B":
            blue = [i, j]
            board[i][j] = "."
            continue
        if board[i][j] == "O":
            goal = [i, j]

direct = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0],
}
min_ = 11


def turn(direction, red, blue):
    goal = "Continue"
    while True:
        next_red = board[red[0] + direct[direction][0]][red[1] + direct[direction][1]]
        if next_red == "#":
            break
        if [red[0] + direct[direction][0], red[1] + direct[direction][1]] == blue:
            next_blue = board[blue[0] + direct[direction][0]][blue[1] + direct[direction][1]]
            if next_blue == "O":
                return ["End", red, blue]
            elif next_blue == ".":
                blue = [blue[0] + direct[direction][0], blue[1] + direct[direction][1]]
                red = [red[0] + direct[direction][0], red[1] + direct[direction][1]]
            elif next_blue == "#":
                break
        elif next_red == "O":
            goal = "Goal"
            red = [0, 0]
            break
        elif next_red == ".":
            red = [red[0] + direct[direction][0], red[1] + direct[direction][1]]

    while True:
        next_blue = board[blue[0] + direct[direction][0]][blue[1] + direct[direction][1]]
        if next_blue == "#":
            break
        elif next_blue == "O":
            return ["End", red, blue]
        elif [blue[0] + direct[direction][0], blue[1] + direct[direction][1]] == red:
            break
        elif next_blue == ".":
            blue = [blue[0] + direct[direction][0], blue[1] + direct[direction][1]]

    return [goal, red, blue]


def turning(moved, red, blue, prev):
    global min_
    if moved >= 11:
        return
    for direction in {"left", "right", "up", "down"} - {prev}:
        res = turn(direction, red, blue)
        result = res[0]
        if result == "Goal" and moved < min_:
            min_ = moved
        elif result == "Continue":
            turning(moved + 1, res[1], res[2], direction)


turning(1, red, blue, 0)
if min_ == 11:
    print(-1)
else:
    print(min_)
