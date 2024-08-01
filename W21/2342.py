import sys, copy
num = list(map(int, sys.stdin.readline().split()))
if len(num) == 1:
    print(0)
    exit(0)
    
INF = 10**7
dict = {
    0: [1,2],
    1: [1,3],
    2: [1,4],
    3: [2,3],
    4: [2,4],
    5: [3,4],
    6: [0,1],
    7: [0,2],
    8: [0,3],
    9: [0,4],
}
feet = [0, num[0]]
dp = [[INF] * (len(num)-1) for i in range(10)]
for i in range(6, 10):
    if dict[i] == feet:
        dp[i][0] = 2
        break

for i in range(1, len(num)-1):
    command = num[i]
    for m in range(10):
        if dp[m][i-1] != INF:
            feet = dict[m]
            if command in feet:
                dp[m][i] = min(dp[m][i], dp[m][i-1]+1)
            else:
                for j in range(2):
                    new_feet = copy.deepcopy(feet)
                    if new_feet[j] == 0:
                        new_effort = 2
                    elif abs(new_feet[j]-command) == 2:
                        new_effort = 4
                    else:
                        new_effort = 3
                    new_feet[j] = command
                    new_feet.sort()
                    for k in range(10):
                        if dict[k] == new_feet:
                            dp[k][i] = min(dp[k][i], dp[m][i-1]+new_effort)
                            break
min_ = INF

for i in range(10):
    min_ = min(min_, dp[i][-1])
print(min_)