import sys


def solution(number, k):
    
    stack = []
    for num in number:
        while stack and int(stack[-1]) < int(num) and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k > 0:
        stack = stack[:-k]
    
    return "".join(stack)
    
    
    