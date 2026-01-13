def solution(numbers):
    answer = []
    for n in numbers:
        string = ""
        while n > 0:
            string = str(n % 2) + string
            n //= 2
        i = 0
        l = len(string)
        while True:
            if (2**i - 1) < l <= 2 ** (i + 1) - 1:
                break
            i += 1
        to_add = "0" * (2 ** (i + 1) - 1 - l)
        real = to_add + string

        if solve(real):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def solve(string):
    l = len(string)
    if l == 1:
        return True
    mid = l // 2
    if string[mid] == "1":
        return solve(string[:mid]) and solve(string[mid + 1 :])
    else:
        comp = "0" * mid
        if string[:mid] == string[mid + 1 :] == comp:
            return True
        else:
            return False
