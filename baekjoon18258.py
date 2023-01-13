from collections import deque
import sys
input=sys.stdin.readline

t = int(input())

deq = deque()

for i in range(t) :
    com = input().split()

    if (com[0] == "push"):
        deq.append(com[1])

    elif (com[0] == "pop"):
        if deq:
            print(deq.popleft())
        else:
            print(-1)
            
    elif (com[0] == "size"):
        print(len(deq))

    elif (com[0] == "empty"):
        if deq:
            print(0)
        else:
            print(1)
            
    elif (com[0] == "front"):
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif (com[0] == "back"):
        if deq:
            print(deq[-1])
        else:
            print(-1)
    



    
#print(deq)
