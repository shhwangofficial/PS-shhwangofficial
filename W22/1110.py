import sys

N = str(sys.stdin.readline()).rstrip()
if len(N) == 1:
    N = "0" + N
temp = N
j = 1
while True:
    num = 0
    for i in range(len(temp)):
        num += int(temp[i])
    num = str(num)
    new = str(temp[-1] + num[-1])

    if new == N:
        print(j)
        exit()
    temp = new
    j += 1
