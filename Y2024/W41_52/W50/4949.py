while True:
    try:
        line = input()
    except EOFError:
        break

    if line == ".":
        break

    stack = []
    for char in line:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")
