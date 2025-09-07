import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
a_b_list = []
for _ in range(N):
    a, b = map(int, input().split())
    a_b_list.append((a, b))

score = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        a = a_b_list[i][0] * a_b_list[j][1]
        b = a_b_list[j][0] * a_b_list[i][1]

        if a < b:
            score[i] += 1
        elif a > b:
            score[j] += 1

ans = [i for i in range(N)]

ans.sort(key=lambda x: -score[x])

for i in ans:
    print(i + 1, end=" ")
