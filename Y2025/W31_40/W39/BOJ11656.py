string = input().strip()
lst = []
for i in range(len(string)):
    lst.append(string[i:])
lst.sort()
for el in lst:
    print(el)
