import sys

N = int(sys.stdin.readline())

nums = []
dic = {}
for _ in range(N):
    temp = int(sys.stdin.readline())
    nums.append(temp)
    if not dic.get(temp, 0):
        dic[temp] = 0
    dic[temp] += 1


print(int(round(sum(nums) / N)))
nums.sort()
print(nums[(len(nums) - 1) // 2])
max_ = 0
i = 0
temp = []
for key in dic:
    if dic[key] > max_:
        max_ = dic[key]
        i = key
        temp = [key]
    elif dic[key] == max_:
        temp.append(key)
temp.sort()
if len(temp) > 1:
    print(temp[1])
else:
    print(i)
print(nums[-1] - nums[0])
