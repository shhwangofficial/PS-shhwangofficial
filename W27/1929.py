import sys
import math
a, b = map(int,sys.stdin.readline().split())
nums = [True] * (b+1)

for i in range(2, int(math.sqrt(b))+2):
    for j in range(2*i, b+1, i):
        nums[j] = False

for i in range(max(2,a), b+1):
    if nums[i] == True:
        print(i)