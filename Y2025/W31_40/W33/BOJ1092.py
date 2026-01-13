import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
cranes.sort()
ans_count = [0] * N
boxes.sort()

if max(boxes) > max(cranes):
    print(-1)
    exit()

for i in range(M - 1, -1, -1):
    tmp = float("inf")
    tmp_idx = -1
    for j in range(N - 1, -1, -1):
        if cranes[j] >= boxes[i]:
            if ans_count[j] < tmp:
                tmp_idx = j
                tmp = ans_count[j]
    ans_count[tmp_idx] += 1

print(max(ans_count))
