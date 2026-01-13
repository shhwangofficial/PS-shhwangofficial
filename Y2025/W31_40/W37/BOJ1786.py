import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

long = input()
short = input()


def build_suffix_array(short):
    res_arr = [0] * len(short)
    i, j = 0, 1
    while j < len(short):
        if short[j] != short[i]:
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
    ans = 0
    location = []
    while i < len(arr_long):
        if arr_long[i] == arr_short[j]:
            if j == len(arr_short) - 1:

                ans += 1
                location.append(i - len(arr_short) + 2)
                i += 1
                j = suffix_arr[j]
                continue
            i += 1
            j += 1
        elif j != 0:
            j = suffix_arr[j - 1]
        else:
            i += 1
    return [ans, location]


suffix_array = build_suffix_array(short)
ans, location = kmp(long, short, suffix_array)
print(ans)
print(*location)
