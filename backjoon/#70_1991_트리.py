import sys
input = sys.stdin.readline

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.root = None

def preorder(pot):
    if pot == '.':
        return 0
    global result
    result += pot
    preorder(data[pot][0])
    preorder(data[pot][1])

def inorder(pot):
    if pot == '.':
        return 0
    global result
    inorder(data[pot][0])
    result += pot
    inorder(data[pot][1])

def postorder(pot):
    if pot == '.':
        return 0
    global result
    postorder(data[pot][0])
    postorder(data[pot][1])
    result += pot

N = int(input())
data = {}
for i in range(N):
    line = input().split()
    data[line[0]] = [line[1], line[2]]

result = ""
preorder('A')
print(result)

result = ""
inorder('A')
print(result)

result = ""
postorder('A')
print(result)

