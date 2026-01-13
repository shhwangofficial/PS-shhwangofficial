import sys

N = int(sys.stdin.readline())
clock1 = sorted(list(map(int, sys.stdin.readline().split())))
clock2 = sorted(list(map(int, sys.stdin.readline().split())))

clock1_diff, clock2_diff = [], []
for i in range(1, N):
    clock1_diff.append(clock1[i] - clock1[i - 1])
    clock2_diff.append(clock2[i] - clock2[i - 1])

clock1_diff.append(360000 + clock1[0] - clock1[-1])
clock2_diff.append(360000 + clock2[0] - clock2[-1])


def build_suffix_array(arr):
    res_arr = [0] * len(arr)
    i, j = 0, 1
    while j < len(arr):
        if arr[j] != arr[i]:
            if i == 0:
                j += 1
            else:
                i = res_arr[i - 1]
        else:
            res_arr[j] = i + 1
            i += 1
            j += 1

    return res_arr


def kmp(arr_long, arr_short, suffix_arr):
    i, j = 0, 0
    while i < len(arr_long):
        if arr_long[i] == arr_short[j]:
            if j == len(arr_short) - 1:
                print("possible")
                return
            i += 1
            j += 1
        elif j != 0:
            j = suffix_arr[j - 1]
        else:
            i += 1
    else:
        print("impossible")
        return


suffix_array = build_suffix_array(clock2_diff)[:]
kmp(clock1_diff + clock1_diff, clock2_diff, suffix_array)
