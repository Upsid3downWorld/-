from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0

L = deque([ i for i in range(1,N+1)])

deq = deque()

for i in range(N):

    cnt = 0

    while L:
        if (cnt == (K-1)):
            deq.append(L.popleft())
            break
        L.append(L.popleft())
        cnt += 1


print("<" , end="")
for i in range(len(deq)-1):
    print("%d, " %(deq[i]), end = "")
print("%d>" %deq[-1])
        
