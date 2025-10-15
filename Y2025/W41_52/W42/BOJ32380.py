import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, U, D = map(int, input().split())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

diff = [0] * (N + 2)
diff2 = [0] * (N + 2)
ans = []


def add_arith(l, r, a, d):
    diff[l] += a
    diff[r + 1] -= a + (r - l) * d
    diff2[l + 1] += d
    diff2[r + 1] -= d


def get_final():
    for i in range(1, N + 1):
        diff2[i] += diff2[i - 1]
        diff[i] += diff[i - 1] + diff2[i]


for i in range(N):
    A = A_lst[i]
    B = B_lst[i]
    ans.append(min(A, B))

    nxt = (B - A) // (U + D)
    if nxt >= 1:
        to, end = i + 1, min(N - 1, i + nxt)
        add_arith(to, end, A + U, U)
    else:
        end = i
    to, end = end + 1, N - 1
    if to <= N - 1:
        initial = B - (to - i) * D
        add_arith(to, end, initial, -D)

get_final()
for i in range(N):
    print(ans[i] + diff[i])
