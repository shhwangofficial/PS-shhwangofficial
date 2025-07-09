import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dic = dict()
dic[1] = set([])
for i in range(1, int(N**0.5) + 1):
    dic[1].add(i**2)

key = 1
while True:
    if N in dic[key]:
        print(key)
        break
    key += 1
    dic[key] = set([])
    for item in dic[key - 1]:
        for sq in dic[1]:
            dic[key].add(item + sq)
