import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()


dr = [-1, 1, 1, -1]
dc = [-1, 1, -1, 1]

R, C = map(int, input().split())

board = [[0] * (2 * C + 1) for _ in range(2 * R + 1)]

for r in range(R):
    line = input()
    for c in range(C):
        board[2 * r + 1][2 * c + 1] = line[c]


def solve():
    NR, NC = 2 * R + 1, 2 * C + 1
    step = 0
    stack = [(0, 0)]
    nxt_stack = set([])
    board[0][0] = 1
    path = ["\\", "\\", "/", "/"]
    while True:
        while stack:
            r, c = stack.pop()
            board[r][c] = 1
            if r == NR - 1 and c == NC - 1:
                print(step)
                return

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < NR and 0 <= nc < NC and board[nr + dr[d]][nc + dc[d]] == 0:
                    if board[nr][nc] == path[d]:
                        board[nr + dr[d]][nc + dc[d]] = 1
                        stack.append((nr + dr[d], nc + dc[d]))
                        nxt_stack.discard((nr + dr[d], nc + dc[d]))

                    else:
                        nxt_stack.add((nr + dr[d], nc + dc[d]))

        if not nxt_stack:
            print("NO SOLUTION")
            return

        stack = list(nxt_stack)
        nxt_stack = set([])
        step += 1


solve()
