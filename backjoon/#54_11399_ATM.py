N = int(input(''))
time_list = list(map(int,input('').split(' ')))
time_list.sort()

i = 0
result = 0
for time in time_list:
    result += time*(N-i)
    i+=1

print(result)