import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

lst = []

for num in nums:
    if not lst or lst[-1] < num:
        lst.append(num)
        continue
    if lst[0] > num:
        lst[0] = num
    else:
        start = 0
        end = len(lst) - 1
        temp_idx = -1
        while start <= end:
            mid = (start + end) // 2
            if lst[mid] < num:
                start = mid + 1
                continue
            else:
                temp_idx = mid
                end = mid - 1
        lst[temp_idx] = num

print(len(lst))
