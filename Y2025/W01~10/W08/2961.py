N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
ans = float("inf")
for bit in range(1, 1 << N):
    temp_S, temp_B = 1, 0
    for i in range(N):
        if bit & (1 << i):
            temp_S *= data[i][0]
            temp_B += data[i][1]
    ans = min(ans, abs(temp_B - temp_S))
print(ans)
