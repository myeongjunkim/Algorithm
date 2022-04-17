import sys
input = sys.stdin.readline

M, N  = map(int,input().split())
hear = [input().strip() for i in range(M)]


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

