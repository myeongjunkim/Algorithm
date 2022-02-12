# T = int(input(''))

# input_list = []
# for i in range(T):
#     input_list.append(list(map(int,input('').split(' '))))
# input_list.sort()

# total = 0

result = []
last_k = list(range(1,15))

for _ in range(10):
    new_k = []
    for i in range(14):
        val = sum(last_k[:i+1])
        new_k.append(val) 
        result.append(new_k)
    last_k = new_k

for r in result:
    print(r)


