import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

max_bit = (1 << N) - 1
for bit in range(1, max_bit + 1):
    tmp = 0
    for digit in range(N):
        if bit & (1 << digit):
            tmp += lst[digit]
    if tmp == S:
        ans += 1
print(ans)
