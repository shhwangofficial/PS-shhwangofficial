import sys

K = int(sys.stdin.readline())

sides = []
for _ in range(6):
    sides.append(list(map(int, sys.stdin.readline().split())))

max_horiz = 0
max_horiz_idx = 0
max_verti = 0
max_verti_idx = 0
for i in range(len(sides)):
    if 1 <= sides[i][0] <= 2:
        if sides[i][1] > max_horiz:
            max_horiz = sides[i][1]
            max_horiz_idx = i
    else:
        if sides[i][1] > max_verti:
            max_verti = sides[i][1]
            max_verti_idx = i

if max_horiz_idx == len(sides) - 1:
    short_verti = abs(sides[max_horiz_idx - 1][1] - sides[0][1])
else:
    short_verti = abs(sides[max_horiz_idx - 1][1] - sides[max_horiz_idx + 1][1])

if max_verti_idx == len(sides) - 1:
    short_horiz = abs(sides[max_verti_idx - 1][1] - sides[0][1])
else:
    short_horiz = abs(sides[max_verti_idx - 1][1] - sides[max_verti_idx + 1][1])

print((max_horiz * max_verti - (short_horiz * short_verti)) * K)
