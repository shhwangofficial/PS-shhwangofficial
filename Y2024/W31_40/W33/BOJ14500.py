import sys

rows, cols = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
shape_long = [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]]
shape_square = [[[0, 0], [0, 1], [1, 0], [1, 1]]]

shape_other = [
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [1, -1], [2, -1]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
]

max_ = 0
for row in range(rows):
    for col in range(cols):
        for shape in shape_long:
            temp = 0
            for point in shape:
                if 0 <= row + point[0] < rows and 0 <= col + point[1] < cols:
                    temp += board[row + point[0]][col + point[1]]
                else:
                    temp = 0
                    continue
            else:
                if max_ < temp:
                    max_ = temp
        for shape in shape_square:
            temp = 0
            for point in shape:
                if 0 <= row + point[0] < rows and 0 <= col + point[1] < cols:
                    temp += board[row + point[0]][col + point[1]]
                else:
                    temp = 0
                    continue
            else:
                if max_ < temp:
                    max_ = temp
        for shape in shape_other:
            for i in range(4):
                for j in range(len(shape)):
                    shape[j][0], shape[j][1] = shape[j][1], -shape[j][0]
                temp = 0
                for point in shape:
                    if 0 <= row + point[0] < rows and 0 <= col + point[1] < cols:
                        temp += board[row + point[0]][col + point[1]]
                    else:
                        temp = 0
                        continue
                else:
                    if max_ < temp:
                        max_ = temp
print(max_)
