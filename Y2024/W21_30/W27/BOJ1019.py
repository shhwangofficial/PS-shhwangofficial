import copy
import math
import sys

N = int(sys.stdin.readline())

memo = dict()
for i in range(1, 10):
    memo[i] = [0] * 10
    for j in range(1, i + 1):
        memo[i][j] = 1


def func(num):
    if num in memo:
        return memo[num]
    else:
        i = 10 ** math.floor(math.log10(num))
        if num % i == 0:
            lst1 = copy.deepcopy(func(num - 1))
            for j in str(num):
                lst1[int(j)] += 1
            memo[num] = lst1
            return memo[num]

        else:
            lst1 = copy.deepcopy(func(num - (num % i)))
            lst2 = copy.deepcopy(func(num % i))

            j = 1
            temp = []

            while 10**j <= i:
                if num % i > 10**j - 1:
                    temp.append(10**j - 1)
                else:
                    temp.append(num % i)
                j += 1

            lst = str(num - (num % i))[-2::-1]
            lst3 = [0] * 10
            for k in range(len(temp)):
                lst3[int(lst[k])] += temp[k]

            memo[num] = [a + b + c for a, b, c in zip(lst1, lst2, lst3)]
            return memo[num]


func(N)
print(*memo[N])
