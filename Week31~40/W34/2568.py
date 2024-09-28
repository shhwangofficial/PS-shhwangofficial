import sys

N = int(sys.stdin.readline())
nums = []
set_A = set()
for _ in range(N):
    input_list = list(map(int, sys.stdin.readline().split()))
    nums.append(input_list)
    set_A.add(input_list[0])

nums.sort()

series = []
idx_list = []
for num in nums:
    if not series:
        series.append(num)
        idx_list.append(0)
    elif series[-1][1] < num[1]:
        series.append(num)
        idx_list.append(len(series) - 1)
    elif series[0][1] > num[1]:
        series[0] = num
        idx_list.append(0)
    else:
        start = 0
        end = len(series) - 1
        while start <= end:
            mid = (start + end) // 2
            if series[mid][1] < num[1]:
                start = mid + 1
            else:
                temp = mid
                end = mid - 1
        series[temp] = num
        idx_list.append(temp)

last_idx = len(series) - 1
set_B = set()
for i in range(len(idx_list) - 1, -1, -1):
    if idx_list[i] == last_idx:
        set_B.add(nums[i][0])
        last_idx -= 1

ans = list(set_A - set_B)
print(len(ans))
for i in sorted(ans):
    print(i)
