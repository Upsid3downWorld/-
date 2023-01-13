from collections import deque
import sys

input=sys.stdin.readline

N = int(input())

deq = deque()

while(True):
    inf = int(input())
    if (inf == -1) :
        break
    elif (inf == 0) :
        deq.popleft()
    else :
        if(len(deq) < N):
            deq.append(inf)
        else:
            continue

if deq:
    print(*deq)
else:
    print("empty")
        
    
