
N = int(input(''))

# 3자리 666

# 4자리 6660 - 9666 > 1666 - 6666 - 6669 - 9666

six_list = [666]
n = 1666
while len(six_list) != N:
    if '666' in str(n):
        six_list.append(n)
    n += 1

print(six_list[-1])