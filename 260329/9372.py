# 백준 9372번

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    for _ in range(M): input()
    
    print(N - 1)


# bfs
import sys
from collections import deque

def bfs(st):
    q = deque([st])
    visited = [False] * (N + 1)
    visited[st] = True
    cnt = 0
    
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                cnt += 1
                q.append(next_node)
                
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    print(bfs(1))


# dfs <- 메모리 초과
import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True
    cnt = 0
    
    for next_node in graph[node]:
        if not visited[next_node]:
            cnt += 1                # 새로운 노드로 갈 때 카운트 +1
            cnt += dfs(next_node)   # 그 노드에서 파고든 누적결과도 더하기
            
    return cnt

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    ans = float('inf')
    
    for i in range(1, N + 1):
        visited = [False] * (N+1)
        ans = min(ans, dfs(i))
        
    print(ans)
