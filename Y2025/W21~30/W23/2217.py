import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
ans = 0
for i in range(N):
    ans = max(ans, nums[i] * (N - i))

print(ans)
