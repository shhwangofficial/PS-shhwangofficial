import sys
formula = list(map(str, sys.stdin.readline().rstrip()))

i = 0
while i < len(formula):
    if formula[i] == "*" or formula[i] == "/":
        if formula[i+1] == "(":
            j = i + 2
            cnt = 1
            while j < len(formula):
                if formula[j] == ")":
                    cnt -= 1
                    if cnt == 0:
                        break
                elif formula[j] == "(":
                    cnt += 1
                j += 1
        else:
            j = i + 2
        formula.insert(j, ")")

        if formula[i-1] == ")":
            j = i-2
            cnt = 1
            while j >= 0:
                if formula[j] == "(":
                    cnt -= 1
                    if cnt == 0:
                        break
                elif formula[j] == ")":
                    cnt += 1                   
                j -= 1
        else:
            j = i - 1
        formula.insert(j, "(")
        i += 1
    i += 1

i = 0
while i < len(formula):
    if formula[i] == "+" or formula[i] == "-":
        if formula[i+1] == "(":
            j = i + 2
            cnt = 1
            while j < len(formula):
                if formula[j] == ")":
                    cnt -= 1
                    if cnt == 0:
                        break
                elif formula[j] == "(":
                    cnt += 1
                j += 1
        else:
            j = i + 2
        formula.insert(j, ")")

        if formula[i-1] == ")":
            j = i-2
            cnt = 1
            while j >= 0:
                if formula[j] == "(":
                    cnt -= 1
                    if cnt == 0:
                        break
                elif formula[j] == ")":
                    cnt += 1
                    
                j -= 1
        else:
            j = i - 1
        formula.insert(j, "(")
        i += 1
    i += 1

i = 0
while i < len(formula):
    if formula[i] == "-":
        if formula[i+1] == "(":
            j = i + 2
            cnt = 1
            while j < len(formula):
                if formula[j] == ")":
                    cnt -= 1
                    if cnt == 0:
                        break
                elif formula[j] == "(":
                    cnt += 1
                j += 1
        else:
            j = i + 2
        formula.insert(j, ")")

        if formula[i-1] == ")":
            j = i-2
            cnt = 1
            while j >= 0:
                if formula[j] == "(":
                    cnt -= 1
                    if cnt == 0:
                        break
                elif formula[j] == ")":
                    cnt += 1
                    
                j -= 1
        else:
            j = i - 1
        formula.insert(j, "(")
        i += 1
    i += 1

i = 0
while i < len(formula):
    if formula[i] == ")":
        del formula[i]
        if formula[i-2] == "(":
            del formula[i-2]
            i -= 2
        else:
            new = formula[i-3] + formula[i-1] + formula[i-2]
            formula[i-3] = new
            del formula[i-1]
            del formula[i-2]
            del formula[i-4]
            i -= 4
    i += 1

print(formula[0])