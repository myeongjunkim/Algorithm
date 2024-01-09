import sys
input = sys.stdin.readline

N = int(input())

result = []
bool_list = [0]*21
for i in range(N):
    line = input().strip().split()
    cmd = line[0]
    if  cmd == 'all':
        bool_list = [1]*21
    elif cmd == 'empty':
        bool_list = [0]*20
    elif cmd == 'add':
        bool_list[int(line[1])] = 1
    elif cmd == 'remove':
        bool_list[int(line[1])] = 0
    elif cmd == 'check':
        print(bool_list[int(line[1])])
    elif cmd == 'toggle':
        bool_list[int(line[1])] = 0 if bool_list[int(line[1])] else 1

