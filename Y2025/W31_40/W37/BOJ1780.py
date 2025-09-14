import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def recur(r, c, size):
    ret = [0, 0, 0]
    for i in range(size):
        for j in range(size):
            if board[r + i][c + j] != board[r][c]:
                new_size = size // 3
                for dr in range(3):
                    for dc in range(3):
                        tmp = recur(r + (new_size * dr), c + (new_size * dc), new_size)
                        ret[0] += tmp[0]
                        ret[1] += tmp[1]
                        ret[2] += tmp[2]
                return ret

    ret[board[r][c]] += 1
    return ret


ans = recur(0, 0, N)
print(ans[-1])
print(ans[0])
print(ans[1])
