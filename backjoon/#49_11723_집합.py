
# def check_cmd(line, set_list, result):
#     cmd = line[0]
#     if cmd == 'add':
#         x = int(line[1])
#         set_list = set_list | set([x])
#     elif cmd == 'remove':
#         x = int(line[1])
#         set_list = set_list - set([x])
#     elif cmd == 'check':
#         x = int(line[1])
#         first_len = len(set_list)
#         set_list = set_list - set([x])
#         last_len = len(set_list)
#         if first_len != last_len:
#             set_list = set_list | set([x])
#             result += "1\n"
#         else:
#             result += "0\n"
#     elif cmd == 'toggle':
#         x = int(line[1])
#         first_len = len(set_list)
#         set_list = set_list - set([x])
#         last_len = len(set_list)
#         if first_len == last_len:
#             set_list = set_list | set([x])
#     elif cmd == 'all':
#         set_list = set(range(1,21))
#     elif cmd == 'empty':
#         set_list = set([])

#     return set_list, result



# N = int(input(''))

# set_list=set([])
# result = ""

# for i in range(N):
#     line = sys.stdin.readline().strip().split(' ')
#     set_list, result = check_cmd(line, set_list, result)
#     del line


# print(result[:-1])


import sys

N = int(input(''))

result = []
bool_list = [False]*20
for i in range(N):
    line = sys.stdin.readline().strip().split(' ')
    cmd = line[0]
    if  cmd == 'all':
        del bool_list
        bool_list = [True]*20
    elif cmd == 'empty':
        del bool_list
        bool_list = [False]*20
    elif cmd == 'add':
        bool_list[int(line[1])-1] = True
    elif cmd == 'remove':
        bool_list[int(line[1])-1] = False
    elif cmd == 'check':
        if bool_list[int(line[1])-1]:
            # result.append(True)

        else:
            # result.append(False)
    elif cmd == 'toggle':
        bool_list[int(line[1])-1] = not bool_list[int(line[1])-1]
    del line, cmd

for _ in result:
    if _:
        print(1)
    else:
        print(0)