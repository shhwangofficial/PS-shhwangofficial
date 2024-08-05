import sys

N = int(sys.stdin.readline())
time_passing = []
for i in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    time_passing.append(num)
cur_time = 0
cur_time += min(time_passing[0][0], time_passing[0][1])
for i in range(1, len(time_passing)):

    green_light = (
        0 <= cur_time % (time_passing[i][2] + time_passing[i][3]) < time_passing[i][2]
    )
    if green_light:
        cur_time += min(time_passing[i][0], time_passing[i][1])
    else:
        remain_time = (
            time_passing[i][2]
            + time_passing[i][3]
            - (cur_time % (time_passing[i][2] + time_passing[i][3]))
        )
        cur_time += min(time_passing[i][0] + remain_time, time_passing[i][1])


print(cur_time)
