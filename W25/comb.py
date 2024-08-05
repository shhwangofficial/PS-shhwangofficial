while True:
    num = list(map(int, input().split()))
    if num == [0]:
        break
    num = num[1:]
    max_num = 6

    def comb(arr, idx):
        if len(arr) == max_num:
            print(*arr)
            return
        for i in range(idx + 1, len(num)):
            comb(arr + [num[i]], i)

    comb([], -1)
    print()
