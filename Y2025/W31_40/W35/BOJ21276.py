import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
name_list = list(map(str, input().split()))
name_list.sort()
ancestor = dict()
cnt_dic = dict()
descedent = dict()
for name in name_list:
    ancestor[name] = []
    cnt_dic[name] = 0
    descedent[name] = []

M = int(input())
for _ in range(M):
    c, p = map(str, input().split())
    ancestor[c].append(p)
    cnt_dic[p] += 1

start = []
for name in name_list:
    if cnt_dic[name] == 0:
        start.append(name)

tmp = []
sijo = []
while start:
    for s in start:
        if ancestor[s]:
            ancestor[s].sort(key=lambda x: cnt_dic[x])
            descedent[ancestor[s][0]].append(s)
            for anc in ancestor[s]:
                cnt_dic[anc] -= 1
            if cnt_dic[ancestor[s][0]] == 0:
                tmp.append(ancestor[s][0])
        else:
            sijo.append(s)
    start = tmp[:]
    tmp = []

sijo.sort()
print(len(sijo))
print(*sijo)
for name in name_list:
    if len(descedent[name]):
        print(name, len(descedent[name]), *sorted(descedent[name]))
    else:
        print(name, 0)
