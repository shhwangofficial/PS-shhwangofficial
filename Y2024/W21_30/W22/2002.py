import sys

N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    dic[string] = _

lst = []
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    lst.append(dic[string])
cnt = 0
for i in range(0, len(lst) - 1):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            cnt += 1
            break
print(cnt)
