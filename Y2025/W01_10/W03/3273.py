import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
aim = int(sys.stdin.readline())
nums.sort()
s, e = 0, N - 1
ans = 0
while s < e:
    if nums[s] + nums[e] == aim:
        ans += 1
        s += 1
    elif nums[s] + nums[e] > aim:
        e -= 1
    elif nums[s] + nums[e] < aim:
        s += 1

print(ans)
