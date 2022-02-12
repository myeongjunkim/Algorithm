N = int(input(''))

import sys
words = [sys.stdin.readline().strip() for i in range(N)]
words = sorted(words,key = lambda x:len(x))

words_len_list=[]
last_word=""
for word in words:
    if word not in words_len_list:
        if len(word) !=len(last_word):
            words_len_list.sort()
            for _ in words_len_list:
                print(_)
            words_len_list=[]
        words_len_list.append(word)
    last_word = word

words_len_list.sort()
for _ in words_len_list:
    print(_)