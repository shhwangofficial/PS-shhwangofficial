import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
max_ = max(nums)
now = 0
for i in range(len(nums)):
    now += nums[i]
    if max_ < now:
        max_ = now
    if now < 0:
        now = 0
    
print(max_)
