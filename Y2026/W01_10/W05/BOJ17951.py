import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

cum_sum = [0]
for num in num_list:
    cum_sum.append(cum_sum[-1] + num)
s, e = 0, sum(num_list)
ans = 0
while s <= e:
    mid = (s + e) // 2
    index = 0
    count = 0
    while index < N:
        pointer = index + 1
        while pointer <= N and cum_sum[pointer] - cum_sum[index] < mid:
            pointer += 1
        if pointer > N:
            break
        count += 1
    
        index = pointer
        
    if count >= K:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
        
print(ans)