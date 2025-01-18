import sys

N = int(sys.stdin.readline())

mydict = {}
lst = []
cnt = 0
for _ in range(N):
    temp = sys.stdin.readline().split()
    city = temp[0]
    city_code = str(city[:2])
    state_code = temp[1]
    new_code = city_code + state_code
    if not mydict.get(new_code, 0):
        mydict[new_code] = 0
    mydict[new_code] += 1
    lst.append(new_code)

for code in lst:
    if code[:2] != code[2:]:
        reverse = str(code[2:] + code[:2])
        if mydict.get(reverse, 0):
            cnt += mydict[reverse]

print(cnt // 2)
