
# # 짝수일 때
# # 나머지 2 >> 2로 나눔 or -1
# # 나머지 1 >> -1 or 2로 나눔 (16 은 2가 유리) (10은 -1이 유리)
# 1 3 3
# 2 2
# 2 1 2
# 1 3 1

# 1 3
# 2 2

# 28 27 9 3 1
# 28 14 7 6 2

# 34 33 11 10
# 34 17 16 8 4 2 1

# 40 20 10
# 40 39 13 

# 64 63 21 7 6 2 1
# 64 32 16 8 4 2 1

# # 홀수 일때
# # 나머지 2 >> -1
# # 나머지 1 >> -1 

# 60002 > 60001 > 60000 > 20000
# 60002 > 30001 > 30000 > 

# 33 11 10 9 3 1
# 33 32 16 8 4 1
# 39 13 12 4 2 1
# 39 38 19 


def make_one(num, cnt):
    if num == 1:
        return cnt
    
    cnt +=1
    if num%3 == 0:
        if num%2 == 1:
            case_1 = make_one(num/3, cnt)
            case_2 = make_one(num-1, cnt)
            if case_1 < case_2:
                return case_1
            return case_2
        else:
            return make_one(num/3, cnt)

    elif num%2 == 0:
        if (num-1)%3 == 0:
            case_1 = make_one(num/2, cnt)
            case_2 = make_one(num-1, cnt)
            if case_1 < case_2:
                return case_1
            return case_2
        else:
            return make_one(num/2, cnt)

    else:
        return make_one(num-1, cnt)


def make_one(num, cnt):
    if num == 1:
        return cnt
    
    cnt +=1
    if num%3 != 0 and num%2 != 0:
        case_1 = make_one(num-1, cnt)
        return case_1
    elif num%3 == 0 and num%2 != 0:
        case_3 = make_one(num/3, cnt)
        case_1 = make_one(num-1, cnt)
        if case_1 < case_3:
            return case_1
        return case_3
    elif num%3 != 0 and num%2 == 0:
        case_2 = make_one(num/2, cnt)
        case_1 = make_one(num-1, cnt)
        if case_1 < case_2:
            return case_1
        return case_2
    else:
        case_3 = make_one(num/3, cnt)
        case_2 = make_one(num/2, cnt)
        case_1 = make_one(num-1, cnt)
        if case_1 < case_2 and case_1 < case_3:
            return case_1
        elif case_2 < case_1 and case_2 < case_3:
            return case_2
        else:
            return case_3




num = int(input())
cnt = 0
print(make_one(num, cnt))

# 실패,,