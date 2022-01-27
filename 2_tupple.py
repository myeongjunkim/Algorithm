# 집합 내{} 에서는 순서 없음.
# 튜플 내에서는 순서 있음.
# 집합으로 들어온걸 튜플로 뱉어라.
# 인풋 문자열은 집합형태로 들어옴.

def solution(s):
    all_parts = str_to_list(s)
    cnt = len(all_parts)
    sorted_parts = [0]*cnt
    dic_parts={}
    for part in all_parts:
        part.sort()
        dic_parts[len(part)] = part

    for k,v in dic_parts.items():
        if k !=1:
            new_set = set(v) - set(dic_parts[k-1])
            sorted_parts[k-1] = list(new_set)[0]
        else:
            sorted_parts[0] = v[0]
    
    return sorted_parts
    
    
    
    
def str_to_list(s):
    stack = []
    all_parts = []
    part = []
    num = ""
    for c in s:
        if c == "{":
            stack.append(c)
        elif c == "}":
            stack.pop()
            if len(stack) == 1:
                part.append(int(num))
                num = ""
            elif len(stack) == 0:
                all_parts.append(part)
                part=[]
        else:
            if len(stack)==2:
                if c == ',':
                    part.append(int(num))
                    num = ""
                else:
                    num = num + c
            elif len(stack)==1:
                all_parts.append(part)
                part=[]
                
    return all_parts