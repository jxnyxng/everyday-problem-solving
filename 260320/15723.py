# 백준 15723번

T = int(input())
arr = [[] for _ in range(27)]

for i in range(T):
    line = input()
    st, ed = line.split(" is ")
    arr[(ord(st)-96)].append((ord(ed)-96))

def check_connection(start, target):
    visited = [False] * 27
    stack = [start]
    visited[start] = True
    
    while stack:
        curr = stack.pop()
        if curr == target:
            return True
        
        for nxt in arr[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    return False

M = int(input())  
for i in range(M):
    line = input()
    st, ed = line.split(" is ")
    
    if check_connection(ord(st)-96, ord(ed)-96):
        print('T')
    else:
        print('F')