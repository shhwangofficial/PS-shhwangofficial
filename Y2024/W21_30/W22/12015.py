import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
my_list = [0]

for num in nums:
    if num > my_list[-1]:
        my_list.append(num)
    elif num <= my_list[1]:
        my_list[1] = num
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
print(len(my_list) - 1)
