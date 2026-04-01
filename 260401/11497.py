# 백준 11497번

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    l.sort(reverse=True)
    res = 0
    
    for i in range(n-2): res = max(res, l[i] - l[i+2])
    
    print(res)
