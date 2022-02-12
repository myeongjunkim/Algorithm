import queue

N = int(input(''))

q = queue.Queue()

for i in range(1,N+1):
    if i%2 == 0:
        q.put(i)

while True:
    i +=1
    top=q.get()
    if q.empty():
        break
    if i%2 == 0:
        q.put(top)

print(top)