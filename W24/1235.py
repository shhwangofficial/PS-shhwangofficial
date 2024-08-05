import sys

N = int(sys.stdin.readline())
list1 = []
for _ in range(N):
    list1.append(sys.stdin.readline().strip())

length = len(list1[0])
for i in range(length - 1, -1, -1):
    s = set()
    for j in list1:
        if j[i:] not in s:
            s.add(j[i:])
        else:
            break
    else:
        print(length - i)
        break
