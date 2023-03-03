"""
구현 문자열 재정렬 322p

K1KA5CB7
-> ABCKK13

AJKDLSI412K4JSJ9D
-> ADDIJJJKKLSS20

"""

import sys
input = sys.stdin.readline

string = input()[:-1]
d_list = []
s_list = []
for s in string:
    if s.isdigit():
        d_list.append(int(s))
    else:
        s_list.append(s)

res = sorted(s_list)
print("".join(res)+str(sum(d_list)))
