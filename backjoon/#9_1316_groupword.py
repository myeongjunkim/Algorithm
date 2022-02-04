def is_group_word(word):
    last_t=""
    char_list=[]
    for c in word:
        if last_t != c:
            if c in char_list:
                return 0
            char_list.append(c)
        last_t = c
    return 1    


T = int(input(''))

cnt = 0
for i in range(T):
    word = input('')
    if is_group_word(word):
        cnt +=1

print(cnt)

