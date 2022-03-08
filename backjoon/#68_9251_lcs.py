import sys
input = sys.stdin.readline


str_1 = input().strip()
str_2 = input().strip()

if len(str_1) < len(str_2):
    str_1, str_2 = str_2, str_1

# [현재 최대, 마지막 index]
dp=[]
if str_1[0] == str_2[0]:
    dp.append([str_1[0]])
else:
    dp.append([str_1[0], str_2[0]])

for i in range(1, len(str_1)):
    

