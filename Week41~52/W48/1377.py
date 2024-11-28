import sys

N = int(sys.stdin.readline())
nums = [(int(sys.stdin.readline()), i) for i in range(N)]

sorted_nums = sorted(nums)

ans = 0
for i in range(len(sorted_nums)):
    ans = max(ans, sorted_nums[i][1] - i)

print(ans + 1)
