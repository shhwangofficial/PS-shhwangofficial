import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

string = input()
close = 0
ans = 0
for i in range(len(string) - 1, -1, -1):
    if string[i] == "(":
        if close == 0:
            ans += 1
        else:
            close -= 1
    elif string[i] == ")":
        close += 1

ans += close
print(ans)
