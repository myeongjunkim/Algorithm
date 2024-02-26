def solution(name):

        
    
    name = list(name)
    
    c_cnt = 0
    for c in name:
        c_cnt += min(ord(c)-ord("A"), ord("Z")-ord(c)+1)
    
    current_name = ["A"]*len(name)
    front, pos = 0, 0
    while True:
        current_name[pos] = name[pos]
        if current_name == name:
            break
        front += 1
        pos += 1
    
    
    min_back = 20
    for i in range(1, len(name)//2+1):
        current_name = ["A"]*len(name)
        back, pos, d = 0, 0, 1
        while True:
            current_name[pos] = name[pos]
            if current_name == name:
                break
            if d > 0 and pos+1 == i:
                d = -1
            back += 1
            pos = (pos+d+len(name))%len(name)
        
        min_back = min(min_back, back)
    
    for i in range(len(name)//2+1, len(name)):
        current_name = ["A"]*len(name)
        back, pos, d = 0, 0, -1
        while True:
            current_name[pos] = name[pos]
            if current_name == name:
                break
            if d < 0 and (pos+d+len(name))%len(name) == i:
                d = 1
            back += 1
            pos = (pos+d+len(name))%len(name)
        min_back = min(min_back, back)

        
    return c_cnt + min(front, min_back)
        
        


