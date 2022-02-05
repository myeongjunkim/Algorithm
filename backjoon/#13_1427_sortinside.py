
N = input('')

result = ""
for c in N:
    new_result = ""
    flag = True
    for r in result:
        if flag and int(c) > int(r):
            new_result += c
            flag = False
        new_result += r
    if flag:
        new_result += c
    result = new_result

print(int(result))