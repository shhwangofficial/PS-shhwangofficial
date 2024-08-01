import sys
a, b = map(int,sys.stdin.readline().split())
my_dogam = {}
for i in range(1, a+1):
    string = sys.stdin.readline().rstrip()
    my_dogam[string] = str(i)
    my_dogam[str(i)] = string

for _ in range(b):
    string = sys.stdin.readline().rstrip()
    print(my_dogam[string])