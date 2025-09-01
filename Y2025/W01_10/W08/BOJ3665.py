T = int(input())
for t in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    pointed = [1] * (n + 1)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            graph[nums[i]][nums[j]] = 1
            pointed[nums[j]] += 1
    for i in range(1, n + 1):
        graph[0][i] = 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if not graph[a][b]:
            a, b = b, a

        graph[a][b] = 0
        graph[b][a] = 1
        pointed[b] -= 1
        pointed[a] += 1

    found = 0
    ans_list = []
    temp = 0
    while True:
        lst = []
        for i in range(1, n + 1):
            if graph[temp][i]:
                pointed[i] -= 1
                if pointed[i] == 0:
                    lst.append(i)
                    ans_list.append(i)
                    found += 1
        if len(lst) == 0 and found != n:
            print("IMPOSSIBLE")
            break
        elif len(lst) > 1:
            print("?")
            break
        elif found == n:
            print(*ans_list)
            break

        temp = lst[0]
