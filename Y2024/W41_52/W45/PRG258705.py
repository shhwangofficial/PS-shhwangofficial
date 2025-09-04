def solution(n, tops):
    import sys

    sys.setrecursionlimit(10**8)
    dic = dict()

    def solve(N, cut):
        if N > n - 1:
            return 1
        if dic.get(2 * N + cut, 0):
            return dic[2 * N + cut]

        if tops[N]:
            if cut:
                dic[2 * N + cut] = (2 * solve(N + 1, 0) + solve(N + 1, 1)) % 10007
            else:
                dic[2 * N + cut] = (3 * solve(N + 1, 0) + solve(N + 1, 1)) % 10007
        else:
            if cut:
                dic[2 * N + cut] = (solve(N + 1, 0) + solve(N + 1, 1)) % 10007
            else:
                dic[2 * N + cut] = (2 * solve(N + 1, 0) + solve(N + 1, 1)) % 10007

        return dic[2 * N + cut]

    return solve(0, 0) % 10007
