import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

lst = []
for num in nums:
    if not lst or lst[-1] < num:
        lst.append(num)
    elif lst[0] > num:
        lst[0] = num
    else:
        start = 0
        end = len(lst) - 1
        while start <= end:
            mid = (start + end) // 2
            if lst[mid] >= num:
                temp = mid
                end = mid - 1
            else:
                start = mid + 1
        lst[temp] = num
print(len(lst))
