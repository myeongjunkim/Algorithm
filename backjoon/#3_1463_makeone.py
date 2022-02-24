import sys
sys.setrecursionlimit(10**6)

def make_one(num, cnt):
    # print(num)
    if num == 1:
        return cnt
    cnt +=1
    case_2, case_3 = -1, -1
    if num %3 == 0:
        case_3 = make_one(num//3, cnt)
    if num %2 == 0:
        case_2 = make_one(num//2, cnt)
    case_1 = make_one(num-1, cnt)
    
    if case_2 == -1:
        if case_3 == -1:
            return case_1
        else:
            return min(case_1, case_3)
    else:
        if case_3 == -1:
            return min(case_1, case_2)
        else:
            return min(case_1, case_2, case_3)



num = int(input())
cnt = 0
print(make_one(num, cnt))

# 실패,,