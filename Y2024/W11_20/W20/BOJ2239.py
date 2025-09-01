import sys

sudoku_map = []
for i in range(9):
    num = list(map(int, sys.stdin.readline().rstrip()))
    sudoku_map.append(num)

blanks = []
for i in range(9):
    for j in range(9):
        if sudoku_map[i][j] == 0:
            blanks.append((i, j))


def term():
    for i in range(9):
        str1 = ""
        for j in range(9):
            str1 += str(sudoku_map[i][j])
        print(str1)
    sys.exit(0)


def solve(start):
    if start == len(blanks):
        term()

    (row, col) = blanks[start]

    sudoku_set = set(sudoku_map[row])
    for i in range(9):
        sudoku_set.add(sudoku_map[i][col])
    for j in range(3):
        for k in range(3):
            sudoku_set.add(sudoku_map[(row // 3) * 3 + j][(col // 3) * 3 + k])

    for val in {1, 2, 3, 4, 5, 6, 7, 8, 9} - sudoku_set:
        sudoku_map[row][col] = val
        ret = solve(start + 1)
        if ret == False:
            (row_, col_) = blanks[start + 1]
            sudoku_map[row_][col_] = 0
        else:
            return ret
    return False


solve(0)
