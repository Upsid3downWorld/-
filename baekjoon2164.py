from collections import deque
import sys

input=sys.stdin.readline

N = int(input())

i = 1

deq = deque()

for k in range(N):
    deq.append(i)
    i += 1

for h in range(N-1):
    deq.popleft()
    #print(deq)
    deq.append(deq[0])
    #print(deq)
    deq.popleft()
    #print(deq)

print(deq[0])
