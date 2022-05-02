# 카카오 채용 연계형 인턴쉽

def solution(s):
    answer = ""
    i=0
    while i != len(s):
        if s[i].isdigit():
            answer+=s[i]
            i+=1       
        elif s[i] == "z":
            answer+="0"
            i+=4
        elif s[i] == "o":
            answer+="1"
            i+=3
        elif s[i] == "t":
            if s[i+1] == "w":
                answer+="2"
                i+=3
            else:
                answer+="3"
                i+=5
        elif s[i] == "f":
            if s[i+1] == "o":
                answer+="4"
                i+=4
            else:
                answer+="5"
                i+=4
        elif s[i] == "s":
            if s[i+1] == "i":
                answer+="6"
                i+=3
            else:
                answer+="7"
                i+=5
        elif s[i] == "e":
            answer+="8"
            i+=5
        elif s[i] == "n":
            answer+="9"
            i+=4 
    
    return int(answer)

