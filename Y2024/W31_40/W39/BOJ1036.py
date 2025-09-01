import sys
from collections import defaultdict

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(N)]
choose = int(sys.stdin.readline())
dic_choose = defaultdict(int)
dic_sum = defaultdict(int)

for word in words:
    word = list(map(str, word.rstrip()))
    i = 0
    for idx in range(len(word) - 1, -1, -1):
        letter = word[idx]
        if ord("0") <= ord(letter) <= ord("9"):
            increment_choose = ord("Z") - 7 - ord(letter)
            increment_sum = ord(letter) - ord("0")
        else:
            increment_choose = ord("Z") - ord(letter)
            increment_sum = ord(letter) - ord("0") - 7
        dic_choose[letter] += increment_choose * (36**i)
        dic_sum[letter] += increment_sum * (36**i)
        i += 1

temp = [[dic_choose[key], key] for key in dic_choose]
temp.sort(reverse=True)

for cnt, top in temp[:choose]:
    dic_sum[top] += cnt

ans_sum = 0
for key in dic_sum:
    ans_sum += dic_sum[key]

ans_lst = []
while ans_sum:
    digit = ans_sum % 36
    if 0 <= digit <= 9:
        ans_lst.append(digit)
    else:
        ans_lst.append(chr(digit + 55))
    ans_sum //= 36

if ans_lst:
    for i in range(len(ans_lst) - 1, -1, -1):
        print(ans_lst[i], end="")
else:
    print(0)
