line = input("")

result = ""
is_b = False
next_index=0
for c in line:
    next_index +=1
    if c == "-":
        if is_b:
            result += ")"
            result += c
            result += "("
        else:
            result += c
            result += "("
            is_b = not is_b
    else:
        if c == '0':
            if next_index<len(line) and line[next_index] in '+-':
                result += c
            elif result == "":
                pass
            elif result[-1] in "+-()":
                pass
            else:
                result += c
        else:
            result += c

if is_b:
    result += ")"

print(eval(result))
