import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

med = {
    (0, 1): 1,
    (1, 0): 1,
}


def dp(tpl):
    W, H = tpl
    if med.get((W, H), 0):
        return med[(W, H)]
    left, right = 0, 0
    if W >= 1:
        left = dp((W - 1, H + 1))
    if H >= 1:
        right = dp((W, H - 1))
    med[(W, H)] = left + right
    return med[(W, H)]


while True:
    N = int(input())
    if N == 0:
        break
    print(dp((N, 0)))
