import sys

N = int(sys.stdin.readline())
mod = 1000000007
mat = {
    1: [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0],
    ],
}


def mat_multiply(arr1, arr2):
    l = len(arr1)
    res = [[0 for j in range(l)] for i in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                res[i][j] += (arr1[i][k] * arr2[k][j]) % mod
            res[i][j] %= mod
    return res


def divide(pow):
    if mat.get(pow, 0):
        return mat[pow]
    i = 1
    while pow > i:
        temp = i
        i *= 2
    if pow == temp:
        mat[pow] = mat_multiply(divide(pow // 2), divide(pow // 2))
    else:
        mat[pow] = mat_multiply(divide(temp), divide(pow - temp))
    return mat[pow]


divide(N)
print(mat[N][0][0])
