import sys

N = int(sys.stdin.readline())

if N % 5 == 0 or N % 5 == 2:
    print("CY")
else:
    print("SK")
