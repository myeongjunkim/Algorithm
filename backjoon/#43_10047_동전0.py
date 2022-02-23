import sys

N, K = map(int,input('').split(' '))

coins=[]
for i in range(N):
    coins.append(int(sys.stdin.readline()))

coins.reverse()

result = 0
cnt = 0
for coin in coins:
    if coin <= K-result:
        needs = ((K-result)//coin)
        result += needs*coin
        cnt += needs
    if result == K:
        break
print(cnt)