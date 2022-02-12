
result=[]
while True:
    N = input('')
    if N =='0':
        break
    n_len = len(N)
    front = N[0:n_len//2]
    if n_len %2 == 0:
        end = N[n_len//2:]
    else:
        end = N[n_len//2+1:]

    if front == end[::-1]:
        result.append('yes')
    else:
        result.append('no')

for _ in result:
    print(_)