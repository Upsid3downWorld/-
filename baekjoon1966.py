from collections import deque
import sys

input = sys.stdin.readline

for i in range(int(input())):

    N, M = map(int, input().split())

    deq = deque(list(map(int, input().split())))

    for j in range(len(deq)):
        deq[j] = (deq[j], j)


    dp = [0]*N # 지워주는 횟수를 저장한다.
    cnt = 0
    while deq:
        if deq[0][0] == max(deq)[0]:
            dp[deq[0][1]] = cnt # cnt는 삭제 했을때의 횟수
            deq.popleft()
            cnt += 1
        else:
            deq.append(deq.popleft())

    print(dp[M]+1)
               
# graph = [ [0] * M for _ in range(N) ]

1012, 2178
