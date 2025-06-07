import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

ans = 0
while True:
    cnt = 0
    for i in range(24):
        if N & (1 << i):
            cnt += 1
    if cnt <= K:
        print(ans)
        break
    for i in range(24):
        if N & (1 << i):
            N += 1 << i
            ans += 1 << i
            break
