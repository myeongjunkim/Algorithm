M, N = map(int, input('').split(' '))

for i in range(min(M, N),0,-1):
    if M%i == 0 and N%i == 0:
        max_common = i
        break

min_common = M*N//max_common


print(max_common)
print(min_common)
