def solution(n, times):
    s = times[0]
    e = max(times) * n
    temp = float("inf")
    while s <= e:
        m = (s + e) // 2

        sum = 0
        for t in times:
            sum += m // t

        if sum >= n:
            e = m - 1
            temp = min(temp, m)
        elif sum < n:
            s = m + 1

    return temp
