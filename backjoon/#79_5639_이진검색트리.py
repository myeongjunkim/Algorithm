import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

num_list = []
while True:
    try:
        num = int(input().strip())
        num_list.append(num)
    except:
        break

print(num_list)


# last_node = None

# for n in num_list:
#     node = Node()
#     node.data = n
#     if n == num_list[0]:
#         head = node
#     elif last_node.data > n:
#         last_node.left = node
#     else:
#         pos_node = head
#         while pos_node.data > n:
#             pos_node = pos_node.left
#         pos_node.right = node
#     last_node = node
