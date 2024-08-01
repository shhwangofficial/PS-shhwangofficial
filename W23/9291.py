import sys
N = int(sys.stdin.readline())

for _ in range(N):
    flag = 0
    sudoku = []
    for i in range(9):
        num = list(map(int, sys.stdin.readline().split()))
        if set(num) != {1,2,3,4,5,6,7,8,9}:
            flag = 1
        sudoku.append(num)
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(sudoku[j][i])
        if set(lst) != {1,2,3,4,5,6,7,8,9}:
            flag = 1
            break
    for i in range(3):
        for j in range(3):
            lst = []
            for k in range(3):
                for l in range(3):
                    lst.append(sudoku[3*i+k][3*j+l])
            if set(lst) != {1,2,3,4,5,6,7,8,9}:
                flag = 1
                break
                
    if flag:
        print(f"Case {_+1}: INCORRECT")
    else:
        print(f"Case {_+1}: CORRECT")
    sys.stdin.readline()