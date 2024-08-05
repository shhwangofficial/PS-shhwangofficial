import sys

N = int(sys.stdin.readline())
mydict = dict()
for _ in range(N):
    arr = list(map(str, sys.stdin.readline().split()))
    arr[1] = int(arr[1])
    arr[2] = int(arr[2])
    arr[3] = int(arr[3])
    arr[1] = arr[1] * 7 + arr[2]
    mydict[arr[0]] = [arr[1], arr[3]]

lst = []
for _ in range(N):
    arr1 = list(map(str, sys.stdin.readline().split()))
    if mydict[arr1[0]][1] <= int(arr1[1]):
        lst.append(mydict[arr1[0]][0])

lst.sort()
if not lst:
    print(0)
else:
    max_count = 1
    cons_cnt = 1
    now_cons = -3

    for i in lst:
        if i - 1 == now_cons:
            cons_cnt += 1
        elif i == now_cons:
            continue
        else:
            cons_cnt = 1
        if cons_cnt > max_count:
            max_count = cons_cnt
        now_cons = i

    print(max_count)
