import sys

N = int(sys.stdin.readline())
dict1 = {}


def add(dic, arr):
    if arr == []:
        return
    if not dic.get(arr[0], 0):
        dic[arr[0]] = {}
    add(dic[arr[0]], arr[1:])


def dfs(dic, num):
    dash = "-" * num
    for key in sorted(dic.keys()):
        print(dash + key)
        dfs(dic[key], num + 2)


for _ in range(N):
    list1 = sys.stdin.readline().split()[1:]
    if not dict1.get(list1[0], 0):
        dict1[list1[0]] = {}

    if len(list1) != 1:
        add(dict1, list1)

dfs(dict1, 0)
