import sys

N = int(sys.stdin.readline())
num = list(map(str, sys.stdin.readline().split()))

if num == ["0"] * N:
    print(0)
    exit()

flag = 1
while flag:
    flag = 0
    for i in range(N - 1):
        if len(num[i]) == len(num[i + 1]):
            if int(num[i + 1]) > int(num[i]):
                flag = 1
                num[i], num[i + 1] = num[i + 1], num[i]

        elif len(num[i + 1]) > len(num[i]):
            a = num[i + 1]
            b = num[i]
            if int(a[: len(b)]) > int(b):
                flag = 1
                num[i], num[i + 1] = num[i + 1], num[i]
            elif int(a[: len(b)]) == int(b):
                if int(b + a[len(b) :]) < int(a[len(b) :] + b):
                    flag = 1
                    num[i], num[i + 1] = num[i + 1], num[i]

        else:
            a = num[i]
            b = num[i + 1]
            if int(a[: len(b)]) < int(b):
                flag = 1
                num[i], num[i + 1] = num[i + 1], num[i]
            elif int(a[: len(b)]) == int(b):
                if int(b + a[len(b) :]) > int(a[len(b) :] + b):
                    flag = 1
                    num[i], num[i + 1] = num[i + 1], num[i]

print("".join(num))
