import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def divide_conquer(board, prev):
    defects = []
    gems = []
    R = len(board)
    if R:
        C = len(board[0])
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                defects.append((r, c))
            elif board[r][c] == 2:
                gems.append((r, c))

    if len(gems) == 0:
        return 0
    if len(gems) == 1 and len(defects) == 0:
        return 1

    ret = 0
    for dr, dc in defects:
        if prev != 1:
            for c in range(C):
                if board[dr][c] == 2:
                    break
                elif board[dr][c] == 1 and c != dc:
                    break
            else:
                ret += divide_conquer(board[:dr], 1) * divide_conquer(board[dr + 1 :], 1)
        if prev != 2:
            for r in range(R):
                if board[r][dc] == 2:
                    break
                elif board[r][dc] == 1 and r != dr:
                    break
            else:
                left, right = [], []
                for r in range(R):
                    left.append(board[r][:dc])
                    right.append(board[r][dc + 1 :])
                ret += divide_conquer(left, 2) * divide_conquer(right, 2)

    return ret


ans = 0
ans = divide_conquer(board, 0)
print(-1 if ans == 0 else ans)
