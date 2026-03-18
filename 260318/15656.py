# 백준 15656번

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
l = []

def dfs(st):
    if len(l) == m:
        print(*l)
        return

    for i in range(st, len(arr)):
        l.append(arr[i])
        dfs(0)
        l.pop()
        
dfs(0)