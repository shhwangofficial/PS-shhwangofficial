import sys

N = int(sys.stdin.readline())

len_str = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

i = 0
cons_lst = []
cons = 0
while i < len_str - 2:
    if string[i] == "O":
        i += 1
        cons = 0
        continue
    else:
        if string[i + 1] == "O" and string[i + 2] == "I":
            cons += 1
            i += 2
        else:
            cons_lst.append(cons)
            i += 1
            cons = 0
cons_lst.append(cons)
cnt = 0
for cons in cons_lst:
    if cons >= N:
        cnt += cons - N + 1
print(cnt)
