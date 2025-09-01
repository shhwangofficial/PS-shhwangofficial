import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
T = int(input())
recom = list(map(int, input().split()))
picture = []
for t in range(T):
    now = recom[t]
    picture.sort(key=lambda x: (-x[1], -x[2]))
    for i in range(len(picture)):
        p, cnt, _ = picture[i]
        if p == now:
            picture[i][1] += 1
            break
    else:
        if len(picture) >= N:
            picture.pop()
        picture.append([now, 1, t])

picture.sort()
for p, cnt, _ in picture:
    print(p, end=" ")
