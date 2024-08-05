import sys

a, b = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()


def recur(arr1, arr2, n):
    if n == 1:
        print(*arr1)
        return
    for j in range(len(arr2)):
        if j >= 1:
            if arr2[j - 1] == arr2[j]:
                continue
        if arr2[j] < arr1[-1]:
            continue

        recur(arr1 + [arr2[j]], arr2, n - 1)
    return


for i in range(len(nums)):
    if i >= 1:
        if nums[i - 1] == nums[i]:
            continue
    recur([nums[i]], nums, b)
