
line = list(map(int,input('').split(' ')))
M, N = line[0], line[1]

import sys
hear = [sys.stdin.readline().strip() for i in range(M)]

hear_watch=[]
for i in range(N):
    watch = sys.stdin.readline().strip()

    new_hear = hear
    l = len(new_hear)
    flag = False
    while l != 0:
        if len(new_hear) == 2 and watch in new_hear:
            flag = True
            break
        l= l//2
        new_hear = new_hear[:l]
        if watch in new_hear:
            flag = True
            break
        else:
            new_hear = new_hear[l:]

    if flag:
        hear_watch.append(watch)

hear_watch.sort()

print(hear_watch)

# for r in hear_watch:
#     print(r)


## 다음에 다시,,,