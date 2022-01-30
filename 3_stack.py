
def try_push(stack, num):
    stack.append(num)

def try_stack(stack, order):
    if order == 'pop':
        if len(stack) != 0:
            return stack.pop()
        return -1
    elif order == 'size':
        return len(stack)
    elif order == 'empty':
        if len(stack) !=0:
            return 0
        return 1
    elif order == 'top':
        if len(stack) !=0:
            return stack[-1]
        return -1

    


cnt = int(input())
stack=[]
results = []
for i in range(cnt):
    order = input()
    if 'push' in order:
        num = int(order.split(' ')[1])
        try_push(stack, num)
    else:
        results.append(try_stack(stack, order))

for re in results:
    print(re)

