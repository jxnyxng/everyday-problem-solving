# 백준 14891번

from collections import deque

def right(idx, d):
    if idx > 3: return
    
    if tooth[idx - 1][2] != tooth[idx][6]:
        right(idx + 1, -d)
        tooth[idx].rotate(d)


def left(idx, d):
    if idx < 0: return
    
    if tooth[idx][2] != tooth[idx + 1][6]:
        left(idx - 1, -d)
        tooth[idx].rotate(d)


tooth = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    # 번호 인덱스 방향
    idx, d = map(int, input().split())
    idx -= 1

    left(idx - 1, -d)
    right(idx + 1, -d)

    tooth[idx].rotate(d)

ans = 0
for i in range(4):
    if tooth[i][0] == 1:
        ans += 2 ** i

print(ans)