import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from math import gcd

D1, D2 = map(int, input().split())
lst_of_everything = [[0] * (D2 + 1) for _ in range(D2 + 1)]
ans = 1
for mother in range(D1, D2 + 1):
    for son in range(1, mother):
        gcd_ms = gcd(mother, son)
        tmp_m, tmp_s = mother // gcd_ms, son // gcd_ms
        if lst_of_everything[tmp_m][tmp_s] == 0:
            ans += 1
            lst_of_everything[tmp_m][tmp_s] = 1


print(ans)
