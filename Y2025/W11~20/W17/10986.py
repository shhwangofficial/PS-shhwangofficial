import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lst = list(map(int, input().split()))

cnt = [0] * (M + 1)
now = 0
for i in range(N):
    now = (now + lst[i]) % M
    cnt[now] += 1


ans = cnt[0]
for i in range(M + 1):
    ans += ((cnt[i]) * (cnt[i] - 1)) // 2

print(ans)
