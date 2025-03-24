import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()


def dfs(string, num):
    if num == N + 1:
        new_string = ""
        for let in string:
            if let != " ":
                new_string += let
        opers = [i for i in new_string if i in ("+", "-")]
        new_string = new_string.replace("-", "+")
        numbers = list(map(int, new_string.split("+")))

        val = numbers[0]
        for i in range(len(opers)):
            if opers[i] == "+":
                val += numbers[i + 1]
            elif opers[i] == "-":
                val -= numbers[i + 1]
        if val == 0:
            print(string)
        return

    dfs(string + " " + str(num), num + 1)
    dfs(string + "+" + str(num), num + 1)
    dfs(string + "-" + str(num), num + 1)


T = int(input())
for _ in range(T):
    N = int(input())
    dfs("1", 2)
    print()
