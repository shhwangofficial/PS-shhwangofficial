# https://www.acmicpc.net/board/view/146355 에 의하여 오류
import sys
N = int(sys.stdin.readline())

mydict = {}
cnt = 0
for i in range(N):
    list1 = sys.stdin.readline().split()
    city = list1[0]
    city_code = str(city[:2])
    state_code = list1[1]
    if not mydict.get(city_code, 0):
        mydict[city_code] = set()
    if not mydict.get(state_code, 0):
        mydict[state_code] = set()

    
    if city_code != state_code:
        for j in mydict[city_code]:
            if j[:2] == state_code:
                cnt += 1
        mydict[state_code].add(city)

print(cnt)
        

