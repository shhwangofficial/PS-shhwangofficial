import sys

def print_func(lotto_num):
    for i in range(len(lotto_num)):
        if lotto_num[i] == 1:
            print(lst_k[i], end=" ")
        if i == len(lotto_num)-1:
            print("")


def lotto(n, lotto_num):
    for i in range(n, len(lotto_num)):
        if lotto_num[i] == 0:
            lotto_num[i] = 1

            if sum(lotto_num) == 6:
                print_func(lotto_num)
                lotto_num[i] = 0
            else:
                lotto(n+1, lotto_num)
        lotto_num[i] = 0

lst = []
while True:
    trial = list(map(int, sys.stdin.readline().split()))
    if trial == [0]:
        break
    lst.append(trial)

for i in range(len(lst)):
    num = lst[i]
    zeros = [0] * num[0]
    lst_k = num[1:]
    lotto(0, zeros)
    if i != len(lst)-1:
        print("")
