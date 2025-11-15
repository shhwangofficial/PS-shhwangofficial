import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))


def solve(lst, attempt, ret):
    start_num, end_num = 0, 0
    if attempt < 2:
        dic = {}  # num -> idx
        for index in range(N):
            dic[lst[index]] = index
        for num in range(1, N + 1):
            if num != dic[num] + 1:
                start_num = num
                break
        for num in range(N, 0, -1):
            if num != dic[num] + 1:
                end_num = num
                break
        # print(start_num, end_num, attempt)
        if start_num:
            new_lst = lst[:]
            to, fr = start_num - 1, dic[start_num]
            sum_ = to + fr
            mid = sum_ // 2
            for i in range(to, mid + 1):
                tmp = lst[sum_ - i]
                new_lst[sum_ - i] = lst[i]
                new_lst[i] = tmp
            solve(new_lst, attempt + 1, ret + [(to + 1, fr + 1)])
        if end_num:
            new_lst = lst[:]
            to, fr = dic[end_num], end_num - 1
            sum_ = to + fr
            mid = sum_ // 2
            for i in range(to, mid + 1):
                tmp = lst[sum_ - i]
                new_lst[sum_ - i] = lst[i]
                new_lst[i] = tmp
            solve(new_lst, attempt + 1, ret + [(to + 1, fr + 1)])

    if not start_num and not end_num:
        for i in range(N):
            if lst[i] != i + 1:
                break
        else:
            for r in ret:
                print(*r)
            for i in range(2 - attempt):
                print("1 1")
            exit()


solve(lst, 0, [])
