# 2021 KAKAO BLIND RECRUITMENT
# ~4:31

"""
조건:
    - 3자 이상 15자 이하 asdf, -, _, .
    - (.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
    
"""

def solution(new_id):
    step1_str = step1(new_id)
    step2_str = step2(step1_str)
    step3_str = step3(step2_str)
    step4_str = step4(step3_str)
    step5_str = step5(step4_str)
    step6_str = step6(step5_str)
    step7_str = step7(step6_str)
    return step7_str

def step1(id):
    return id.lower() 

def step2(id):
    new_id = []
    for c in id:
        if c.isalpha() or c in "1234567890" or c in "-_.":
            new_id.append(c)
    return "".join(new_id)

def step3(id):
    while ".." in id:
        id = id.replace("..",".")
    return id

def step4(id):
    if id == ".":
        return ""
    if id[0] == ".":
        id = id[1:]
    if id[-1] == ".":
        id = id[:-1]
    return id

def step5(id):
    if id == "":
        return "a"
    return id

def step6(id):
    if len(id) >= 16:
        id = id[:15]
    while id[-1] == ".":
        id = id[:-1]
    return id

def step7(id):
    while len(id) <= 2:
        id = id+id[-1]
    return id
        
        