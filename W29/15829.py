import sys
N = int(sys.stdin.readline())
string = list(map(str, sys.stdin.readline().rstrip()))
M = 1234567891
sum_ = 0
for i, letter in enumerate(string):
    sum_ += (ord(letter)-ord('a')+1) * (31**i)
    sum_ %= M

print(sum_)

