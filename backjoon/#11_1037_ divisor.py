T = int(input(''))

if T == 1:
    print(int(input(''))**2)
else:
    divisor_list = list(map(int,input('').split(' ')))
    divisor_list.sort()
    print(divisor_list[0]*divisor_list[-1])