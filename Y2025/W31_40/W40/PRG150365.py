def solution(n, m, x, y, r, c, k):
    import sys

    sys.setrecursionlimit(5000)

    answer = ""
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    dir = {0: "d", 1: "l", 2: "r", 3: "u"}

    def time_to_solve_real(x, y, k):
        tmp = ""
        need_to_move_y = c - y
        need_to_move_x = r - x
        if need_to_move_x >= 0:
            tmp += "d" * (need_to_move_x)
            if need_to_move_y < 0:
                tmp += "l" * (-need_to_move_y)
            else:
                tmp += "r" * (need_to_move_y)
        else:
            if need_to_move_y < 0:
                tmp += "l" * (-need_to_move_y)
            else:
                tmp += "r" * (need_to_move_y)
            tmp += "u" * (-need_to_move_x)
        return tmp

    def find_nangbi_move(x, y):
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            if 0 <= nx < n and 0 <= ny < m:
                return dir[i], nx, ny

    def solve(x, y, k, path):
        manhattan = abs(x - r) + abs(y - c)
        if k == manhattan:
            path += time_to_solve_real(x, y, k)
            return path
        elif k < manhattan:
            return False
        elif k % 2 != manhattan % 2:
            return False
        else:
            d, newx, newy = find_nangbi_move(x, y)
            return solve(newx, newy, k - 1, path + d)

    answer = solve(x, y, k, "")
    if not answer:
        return "impossible"

    return answer
