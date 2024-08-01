import sys
a, b = map(int,sys.stdin.readline().split())
list1 = sys.stdin.readline().split()


ans1 = 0
temp1 = 0
ans2 = 0
temp2 = 0
for i in range(len(list1)):
    if list1[i] == "Fizz":
        ans1 = i+a - temp1
        temp1 = i+a
    elif list1[i] == "Buzz":
        ans2 = i+a - temp2
        temp2 = i+a
    elif list1[i] == "FizzBuzz":
        ans1 = i+a - temp1
        temp1 = i+a
        ans2 = i+a - temp2
        temp2 = i+a
if ans1 == 0:
    ans1 = b+1
if ans2 == 0:
    ans2 = b+1
print(ans1, ans2)