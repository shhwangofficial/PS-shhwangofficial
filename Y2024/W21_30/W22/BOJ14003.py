import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
my_list = []
my_idx_list = []
for num in nums:
    if not my_list:
        my_list.append(num)
        my_idx_list.append(len(my_list) - 1)
    elif num > my_list[-1]:
        my_list.append(num)
        my_idx_list.append(len(my_list) - 1)
    elif num <= my_list[0]:
        my_list[0] = num
        my_idx_list.append(0)
    else:
        left = 0
        right = len(my_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if my_list[mid] < num:
                left = mid + 1
            else:
                idx = mid
                right = mid - 1
        my_list[idx] = num
        my_idx_list.append(idx)
print(len(my_list))
LIS = []
max_ = len(my_list) - 1
for i in range(len(my_idx_list) - 1, -1, -1):
    if my_idx_list[i] == max_:
        LIS.append(nums[i])
        max_ -= 1

print(*sorted(LIS))
