import sys

K, N = map(int, sys.stdin.readline().split())
nums = []
for i in range(K):
    nums.append(sys.stdin.readline().strip())
nums.sort(key=lambda x: (int(x)), reverse=True)
longest = nums[0]
for i in range(N - K):
    nums.append(longest)
nums.sort(key=lambda x: x * 10, reverse=True)
print("".join(nums))
