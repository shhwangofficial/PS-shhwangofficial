import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    input_list = list(map(int, sys.stdin.readline().split()))
    nums.append(input_list)

nums.sort()

series = []
idx_list = []
for num in nums:
    if not series:
        series.append(num)
    elif series[-1][1] < num[1]:
        series.append(num)
    elif series[0][1] > num[1]:
        series[0] = num
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

print(N - len(series))
