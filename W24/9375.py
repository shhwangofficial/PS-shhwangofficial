import sys

T = int(sys.stdin.readline())
for _ in range(T):
    my_dict = {}
    N = int(sys.stdin.readline())
    for i in range(N):
        num = list1 = sys.stdin.readline().split()
        if not my_dict.get(num[1], 0):
            my_dict[num[1]] = 0
        my_dict[num[1]] += 1
    i = 1
    for j in my_dict.keys():
        i *= my_dict[j] + 1
    print(i - 1)
