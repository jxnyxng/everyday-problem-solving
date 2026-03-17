# 백준 13417번
from collections import deque

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    l = list(input().split())
    dq = deque()
    
    for a in l:
        if len(dq) == 0:
            dq.append(a)
        else:
            if ord(dq[0]) >= ord(a):
                dq.appendleft(a)
            else:
                dq.append(a)

    ans.append(''.join(dq))

print('\n'.join(ans))