import sys
from math import ceil

N, H_Att = map(int, sys.stdin.readline().split())

room_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
has_to_remain = 1
max_hp_ans = 0
cur_hp = 0

for room in room_list:
    if room[0] == 2:
        H_Att += room[1]

for i in range(N - 1, -1, -1):
    type_, att, hp = room_list[i]
    if type_ == 1:
        cur_hp = (ceil((hp / H_Att)) - 1) * att + has_to_remain
        if cur_hp > max_hp_ans:
            max_hp_ans = cur_hp
        has_to_remain = cur_hp

    elif type_ == 2:
        H_Att -= att
        has_to_remain -= hp
        if has_to_remain <= 0:
            has_to_remain = 1

print(max_hp_ans)
