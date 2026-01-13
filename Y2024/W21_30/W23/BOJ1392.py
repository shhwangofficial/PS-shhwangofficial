a, b = map(int, input().split())
lst = []
k = 1
for i in range(a):
    c = int(input())
    for j in range(c):
        lst.append(k)
    k += 1

for i in range(b):
    c = int(input())
    print(lst[c])
