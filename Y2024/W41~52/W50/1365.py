import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

lst = []
for i in num:
    if not lst or lst[-1] < i:
        lst.append(i)
    else:
        s, e = 0, len(lst) - 1
        while s <= e:
            mid = (s + e) // 2
            if lst[mid] > i:
                temp = mid
                e = mid - 1
            else:
                s = mid + 1
        lst[temp] = i


print(N - len(lst))
