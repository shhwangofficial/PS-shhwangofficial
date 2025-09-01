import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import math

N, K = map(int, input().split())
dic = dict()
for i in range(1, N + 1):
    dic[i] = math.ceil(i / 2) * (i // 2)


lst = []
if K > dic[N]:
    for i in range(N - 1, 0, -1):
        deficit = K - dic[i]
        now = N - i
        if i * now >= deficit:
            while deficit > 0:
                a = min(deficit, i)
                lst.append(a)
                deficit -= a
            K = dic[i]
            N = i
            break
    else:
        print(-1)
        exit()

ans = ["A"] * math.ceil(N / 2) + ["B"] * (N // 2)
for i in range(dic[N] - K):
    for j in range(len(ans) - 1):
        if ans[j] == "A" and ans[j + 1] == "B":
            ans[j] = "B"
            ans[j + 1] = "A"
            break
if not lst:
    print("".join(ans))
else:
    for i in lst:
        ans.insert(i, "C")
    print("".join(ans))
